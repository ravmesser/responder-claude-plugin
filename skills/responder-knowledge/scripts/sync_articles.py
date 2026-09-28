#!/usr/bin/env python3
"""Mirror the Responder knowledge base into this skill for offline use."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import sys
import time
import unicodedata
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from zipfile import ZIP_DEFLATED, ZipFile

import trafilatura
from lxml import html as lxml_html


BASE_URL = "https://support.responder.co.il/portal/he/kb/responderlive"
ARTICLE_PATH = "/portal/he/kb/articles/"
CATEGORY_PATH = "/portal/he/kb/responderlive/"
INDEX_START = "<!-- BEGIN GENERATED OFFLINE ARTICLE INDEX -->"
INDEX_END = "<!-- END GENERATED OFFLINE ARTICLE INDEX -->"
ARTICLE_URL_RE = re.compile(r"https://support\.responder\.co\.il/portal/he/kb/articles/[^\s)`>]+")


@dataclass(frozen=True)
class Page:
    url: str
    title: str
    content: str
    category: str


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()
        self.title_parts: list[str] = []
        self.heading_parts: list[str] = []
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.add(href)
        elif tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._in_h1:
            self.heading_parts.append(data)

    @property
    def title(self) -> str:
        value = " ".join(self.title_parts) or " ".join(self.heading_parts)
        return clean_title(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=BASE_URL, help="Knowledge-base root URL")
    parser.add_argument("--delay", type=float, default=0.15, help="Seconds between requests")
    return parser.parse_args()


def canonical_url(url: str) -> str:
    parts = urlsplit(url)
    path = quote(unquote(re.sub(r"/+$", "", parts.path)), safe="/:@")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def clean_title(value: str) -> str:
    value = html.unescape(re.sub(r"\s+", " ", value)).strip()
    return re.sub(r"\s*[|–-]\s*רב מסר.*$", "", value).strip()


def title_from_url(url: str) -> str:
    return clean_title(unquote(urlsplit(url).path.rsplit("/", 1)[-1]).replace("-", " "))


def safe_filename(title: str, url: str) -> str:
    normalized = unicodedata.normalize("NFKC", title).lower()
    normalized = re.sub(r"[^\w\u0590-\u05ff]+", "-", normalized, flags=re.UNICODE).strip("-_")
    normalized = normalized[:120].rstrip("-_") or "article"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"{normalized}-{digest}.md"


def fetch(url: str, delay: float) -> str:
    if delay:
        time.sleep(delay)
    request = Request(
        url,
        headers={
            # Zoho returns a client-rendered shell to browser user-agents, while
            # its curl-compatible response contains the server-rendered links.
            "User-Agent": "curl/8.7.1",
            "Accept": "*/*",
            "Accept-Language": "he,en;q=0.8",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except OSError as error:
        raise RuntimeError(f"Failed to download {url}: {error}") from error


def parse_document(document: str) -> LinkParser:
    parser = LinkParser()
    parser.feed(document)
    # Zoho's help-center HTML occasionally contains markup that HTMLParser skips.
    # Keep discovery resilient by collecting literal href attributes as a fallback.
    parser.links.update(
        html.unescape(match)
        for match in re.findall(r"href\s*=\s*[\"']([^\"']+)[\"']", document, re.IGNORECASE)
    )
    return parser


def without_related_articles(document: str) -> str:
    try:
        tree = lxml_html.fromstring(document)
    except (ValueError, lxml_html.etree.ParserError):
        return document
    for element in tree.xpath(
        "//*[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'related_artic')]"
    ):
        element.drop_tree()
    for element in tree.xpath(
        "//h1[translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz') = 'related articles']/ancestor::ul[1]"
    ):
        element.drop_tree()
    return lxml_html.tostring(tree, encoding="unicode", method="html")


def discover(base_url: str, delay: float) -> dict[str, set[str]]:
    base_url = canonical_url(base_url)
    host = urlsplit(base_url).netloc
    queue: deque[str] = deque([base_url])
    visited: set[str] = set()
    article_categories: dict[str, set[str]] = defaultdict(set)

    while queue:
        category_url = queue.popleft()
        if category_url in visited:
            continue
        visited.add(category_url)
        document = fetch(category_url, delay)
        parsed = parse_document(document)
        category = "General" if category_url == base_url else title_from_url(category_url)

        for href in sorted(parsed.links):
            url = canonical_url(urljoin(category_url, href))
            parts = urlsplit(url)
            if parts.netloc != host:
                continue
            if parts.path.startswith(ARTICLE_PATH):
                article_categories[url].add(category)
            elif parts.path.startswith(CATEGORY_PATH) and url not in visited:
                queue.append(url)

        print(
            f"Discovered {category}: {len(parsed.links)} links, "
            f"{len(article_categories)} articles total",
            file=sys.stderr,
        )

    if not article_categories:
        raise RuntimeError("No articles were discovered; the help-center structure may have changed")
    return article_categories


def extract_page(url: str, categories: set[str], delay: float) -> Page:
    document = fetch(url, delay)
    parsed = parse_document(document)
    title = parsed.title or title_from_url(url)
    document = without_related_articles(document)
    content = trafilatura.extract(
        document,
        output_format="markdown",
        include_comments=False,
        include_links=False,
        include_images=False,
        include_tables=True,
        deduplicate=True,
        favor_recall=True,
    )
    if not content or len(content.strip()) < 40:
        raise RuntimeError(f"Trafilatura extracted no useful content from {url}")
    content = re.split(
        r"(?im)^\s*(?:-\s*)?#+\s+Related Articles\s*$", content.strip(), maxsplit=1
    )[0].rstrip()
    return Page(url=url, title=title, content=content.strip(), category=sorted(categories)[0])


def render_article(page: Page) -> str:
    content = page.content
    duplicate_heading = re.compile(rf"^#+\s+{re.escape(page.title)}\s*\n+", re.IGNORECASE)
    content = duplicate_heading.sub("", content, count=1)
    return f"# {page.title}\n\nCategory: {page.category}\n\n{content}\n"


def render_catalog(pages: list[Page], filenames: dict[str, str], generated_at: str) -> str:
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        grouped[page.category].append(page)

    lines = [
        "# Offline Responder article catalog",
        "",
        f"Generated from the official Responder knowledge base at {generated_at}.",
        "Search this directory with `rg -n \"<Hebrew or English term>\" references/articles/`.",
        "",
        "## Categories",
        "",
    ]
    for category in sorted(grouped):
        anchor = re.sub(r"[^\w\u0590-\u05ff -]", "", category, flags=re.UNICODE).strip().lower().replace(" ", "-")
        lines.append(f"- [{category}](#{anchor}) — {len(grouped[category])} articles")
    for category in sorted(grouped):
        lines.extend(["", f"## {category}", ""])
        for page in sorted(grouped[category], key=lambda item: item.title):
            lines.append(f"- [{page.title}]({filenames[page.url]})")
    return "\n".join(lines) + "\n"


def generated_skill_index(pages: list[Page], generated_at: str) -> str:
    counts: dict[str, int] = defaultdict(int)
    for page in pages:
        counts[page.category] += 1
    lines = [
        INDEX_START,
        "### Offline article corpus (generated)",
        "",
        f"The complete local corpus contains **{len(pages)} articles**, refreshed {generated_at}.",
        "Read `references/articles/INDEX.md` to find an article by category or title, or search",
        "`references/articles/` with `rg`. These files are sufficient for answering without internet access.",
        "",
    ]
    lines.extend(f"- {category}: {counts[category]} articles" for category in sorted(counts))
    lines.append(INDEX_END)
    return "\n".join(lines)


def update_skill_index(skill_path: Path, block: str) -> None:
    content = skill_path.read_text(encoding="utf-8")
    if INDEX_START in content and INDEX_END in content:
        pattern = re.compile(rf"{re.escape(INDEX_START)}.*?{re.escape(INDEX_END)}", re.DOTALL)
        content = pattern.sub(block, content, count=1)
    else:
        content = content.rstrip() + "\n\n" + block + "\n"
    skill_path.write_text(content, encoding="utf-8")


def rewrite_curated_links(references_dir: Path, filenames: dict[str, str]) -> None:
    filenames_by_digest = {
        filename.removesuffix(".md").rsplit("-", 1)[-1]: filename
        for filename in filenames.values()
    }
    local_article_re = re.compile(r"articles/[^)\s]+-([0-9a-f]{8})\.md")
    for path in sorted(references_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")

        def replace(match: re.Match[str]) -> str:
            raw_url = match.group(0)
            trailing = raw_url[len(raw_url.rstrip(".,;:")) :]
            url = canonical_url(raw_url.rstrip(".,;:"))
            filename = filenames.get(url)
            replacement = (
                f"[offline article](articles/{filename})"
                if filename
                else "[offline article catalog](articles/INDEX.md)"
            )
            return replacement + trailing

        updated = ARTICLE_URL_RE.sub(replace, content)

        def refresh_local_link(match: re.Match[str]) -> str:
            filename = filenames_by_digest.get(match.group(1))
            return f"articles/{filename}" if filename else "articles/INDEX.md"

        updated = local_article_re.sub(refresh_local_link, updated)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def publish(skill_dir: Path, pages: list[Page]) -> None:
    references_dir = skill_dir / "references"
    target_dir = references_dir / "articles"
    temporary_dir = references_dir / ".articles.tmp"
    if temporary_dir.exists():
        shutil.rmtree(temporary_dir)
    temporary_dir.mkdir(parents=True)

    filenames = {page.url: safe_filename(page.title, page.url) for page in pages}
    generated_at = datetime.now(timezone.utc).date().isoformat()
    for page in pages:
        (temporary_dir / filenames[page.url]).write_text(render_article(page), encoding="utf-8")
    (temporary_dir / "INDEX.md").write_text(render_catalog(pages, filenames, generated_at), encoding="utf-8")

    if target_dir.exists():
        shutil.rmtree(target_dir)
    temporary_dir.rename(target_dir)
    rewrite_curated_links(references_dir, filenames)
    update_skill_index(skill_dir / "SKILL.md", generated_skill_index(pages, generated_at))


def create_skill_zip(skill_dir: Path) -> Path:
    archive_path = skill_dir.with_suffix(".zip")
    temporary_path = archive_path.with_name(f"{archive_path.name}.tmp")
    excluded_parts = {"__pycache__", ".DS_Store"}
    temporary_path.unlink(missing_ok=True)

    try:
        with ZipFile(
            temporary_path,
            mode="w",
            compression=ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for path in sorted(skill_dir.rglob("*")):
                relative_path = path.relative_to(skill_dir)
                if not path.is_file():
                    continue
                if excluded_parts.intersection(relative_path.parts) or path.suffix == ".pyc":
                    continue
                archive.write(path, Path(skill_dir.name) / relative_path)
        temporary_path.replace(archive_path)
    finally:
        temporary_path.unlink(missing_ok=True)

    return archive_path


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    try:
        article_categories = discover(args.base_url, args.delay)
        pages = []
        for number, (url, categories) in enumerate(sorted(article_categories.items()), start=1):
            print(f"Extracting {number}/{len(article_categories)}: {title_from_url(url)}", file=sys.stderr)
            pages.append(extract_page(url, categories, args.delay))
        publish(skill_dir, pages)
        archive_path = create_skill_zip(skill_dir)
    except (OSError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Saved {len(pages)} articles under {skill_dir / 'references' / 'articles'}")
    print(f"Created skill archive at {archive_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
