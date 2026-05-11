from __future__ import annotations

import html
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = REPO_ROOT / "solutions"
DOCS_DIR = REPO_ROOT / "docs"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def _extract_primary_category(readme_text: str) -> str | None:
    """
    One primary category per solution: first line matching Primary category: ...
    Ignores secondary tags and other fields.
    """
    for raw in readme_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(
            r"^(?:-\s+)?(?:\*\*)?Primary category:(?:\*\*)?\s*(.+?)\s*$",
            line,
            re.IGNORECASE,
        )
        if m:
            return m.group(1).strip()
    return None


def _extract_h1_title(readme_text: str) -> str:
    for raw in readme_text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _slug_to_label(slug: str) -> str:
    return slug.replace("-", " ").strip().title()


def _normalize_category_key(name: str) -> str:
    """Merge spelling variants (case, extra spaces) into one bucket."""
    return " ".join(name.split()).casefold()


_README_CATALOG_START = "## 📂 Quick Access Solutions Catalog"
_README_SECURITY_START = "## Security & Privacy"


def _copy_repo_images_to_docs() -> None:
    """MkDocs serves only under docs_dir; mirror repo img/ for README assets."""
    src = REPO_ROOT / "img"
    if not src.is_dir():
        return
    dest = DOCS_DIR / "img"
    dest.mkdir(parents=True, exist_ok=True)
    for p in src.iterdir():
        if p.is_file():
            shutil.copy2(p, dest / p.name)


def _rewrite_readme_links_for_docs(md: str) -> str:
    """Point ./solutions/... links at generated doc pages; keep img/ and absolute URLs."""

    def repl(m: re.Match[str]) -> str:
        rest = (m.group(1) or "").strip().strip("/")
        if rest.endswith("README.md"):
            rest = rest[: -len("README.md")].rstrip("/")
        if not rest:
            return "](#browse-by-category)"
        return f"]({rest}/)"

    md = re.sub(r"\]\(\./solutions/?([^)]*)\)", repl, md)
    return md


def _readme_body_for_docs_index() -> str | None:
    """
    Root docs page follows repo README.md: drop the long GitHub-only catalog block,
    keep product story + legal/contributing tail. Returns None if README missing.
    """
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        return None
    text = readme_path.read_text(encoding="utf-8", errors="replace")
    i = text.find(_README_CATALOG_START)
    j = text.find(_README_SECURITY_START)
    if i != -1 and j != -1 and j > i:
        head = re.sub(r"\n---\s*$", "", text[:i].rstrip())
        tail = text[j:].lstrip()
        text = head + "\n\n---\n\n" + tail
    text = _rewrite_readme_links_for_docs(text)
    return text


def _categories_appendix_lines(category_to_solutions: dict[str, list[tuple[str, str]]]) -> list[str]:
    """Markdown block: category table + expandable lists (anchor browse-by-category)."""
    total_slugs = sum(len(v) for v in category_to_solutions.values())
    cat_keys = sorted(category_to_solutions.keys(), key=lambda s: s.lower())

    lines: list[str] = [
        "## Categories",
        "",
        "Each template lists exactly **one** primary category in its README (`Primary category:`). "
        "Solutions appear once under that category.",
        "",
        "| Category | Templates |",
        "| --- | ---: |",
    ]
    for cat in cat_keys:
        n = len(category_to_solutions[cat])
        anchor = _category_anchor(cat)
        lines.append(f"| [{cat}](#{anchor}) | {n} |")
    lines.append("")
    lines.append(f"**Total:** {total_slugs} templates in **{len(cat_keys)}** categories.")
    lines.append("")
    lines.append("## Browse by category")
    lines.append("")

    for cat in cat_keys:
        pairs = sorted(category_to_solutions[cat], key=lambda p: p[1].lower())
        anchor = _category_anchor(cat)
        lines.append(f'<h3 id="{html.escape(anchor, quote=True)}">{html.escape(cat)}</h3>')
        lines.append("")
        lines.append("<details>")
        lines.append("<summary><strong>Expand list</strong></summary>")
        lines.append("")
        for slug, title in pairs:
            lines.append(f"- [{title}]({slug}/)")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return lines


def _write_docs_index(category_to_solutions: dict[str, list[tuple[str, str]]]) -> None:
    """category -> [(slug, page_title), ...]. Root page mirrors README.md + generated catalog."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    _copy_repo_images_to_docs()

    readme_part = _readme_body_for_docs_index()
    appendix = _categories_appendix_lines(category_to_solutions)

    if readme_part is not None:
        parts: list[str] = [readme_part.rstrip(), "", "---", "", *appendix]
    else:
        parts = [
            "# Uplizd Solutions",
            "",
            "Browse thousands of ready-made AI workflow templates. Each page is indexed separately so search engines "
            "and site search can surface the exact solution you need.",
            "",
            "---",
            "",
            *appendix,
        ]

    (DOCS_DIR / "index.md").write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8", newline="\n")


def _unique_sidebar_label(title: str, slug: str, seen: set[str]) -> str:
    base = (title or "").strip() or _slug_to_label(slug)
    label = base
    if label not in seen:
        seen.add(label)
        return label
    label = f"{base} ({slug})"
    if label not in seen:
        seen.add(label)
        return label
    n = 2
    while True:
        cand = f"{base} ({slug}) [{n}]"
        if cand not in seen:
            seen.add(cand)
            return cand
        n += 1


def _write_docs_pages_yml(category_to_solutions: dict[str, list[tuple[str, str]]]) -> None:
    """
    Sidebar nav for mkdocs-awesome-pages-plugin.

    Nesting: Home → Browse by category → <Primary category> → solution pages.
    Material then shows category labels and groups pages under each category (not a flat list).
    """
    cat_keys = sorted(category_to_solutions.keys(), key=lambda s: s.lower())
    category_blocks: list[dict[str, list[dict[str, str]]]] = []

    for cat in cat_keys:
        pairs = sorted(category_to_solutions[cat], key=lambda p: p[1].lower())
        seen: set[str] = set()
        children: list[dict[str, str]] = []
        for slug, title in pairs:
            label = _unique_sidebar_label(title, slug, seen)
            children.append({label: f"{slug}/index.md"})
        category_blocks.append({cat: children})

    nav: list[object] = [
        {"Home": "index.md"},
        {"Browse by category": category_blocks},
    ]

    body = yaml.safe_dump(
        {"nav": nav},
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=10000,
        indent=2,
    )
    header = (
        "# Generated by scripts/generate_docs.py — do not edit by hand.\n"
        "# Re-run: python scripts/generate_docs.py\n\n"
    )
    (DOCS_DIR / ".pages.yml").write_text(header + body, encoding="utf-8", newline="\n")


def _category_anchor(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", name)
    s = re.sub(r"\s+", "-", s.strip()).lower()
    return s or "category"


def _rewrite_local_image_links(md: str) -> str:
    """
    Rewrite local image links like ![](image.png) to ![](assets/image.png).
    Keep absolute URLs and paths that already contain a slash unchanged.
    """

    def repl(match: re.Match[str]) -> str:
        alt = match.group("alt")
        url = match.group("url").strip()

        # Leave remote or anchored URLs unchanged
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url) or url.startswith("#"):
            return match.group(0)

        # If it's already a path (has a slash), don't guess.
        if "/" in url or "\\" in url:
            return match.group(0)

        ext = Path(url).suffix.lower()
        if ext in IMAGE_EXTS:
            return f"![{alt}](assets/{url})"

        return match.group(0)

    return re.sub(r"!\[(?P<alt>[^\]]*)\]\((?P<url>[^)]+)\)", repl, md)


def _rewrite_solution_readme_links(md: str) -> str:
    """
    Many solution READMEs link to sibling solutions via ../other-solution/README.md.
    In the docs site, each solution lives at ../other-solution/ (index.md).
    """

    def repl(match: re.Match[str]) -> str:
        text = match.group("text")
        url = match.group("url").strip()

        # Leave remote URLs unchanged
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
            return match.group(0)

        # Rewrite README.md links to docs index.md.
        # Examples:
        # - ../other-solution/README.md  -> ../other-solution/index.md
        # - ./README.md                 -> index.md
        url2 = url
        url2 = re.sub(r"(^\./)?README\.md(\b|[#?].*)?$", r"index.md\2", url2)
        url2 = re.sub(r"(^|/)(README\.md)(\b|[#?].*)?$", r"\1index.md\3", url2)

        # If the URL ends with a slash (../other-solution/), mkdocs wants index.md explicitly.
        url2 = re.sub(r"(?<!/)/(\s*)$", r"/index.md\1", url2)

        if url2 != url:
            return f"[{text}]({url2})"

        return match.group(0)

    return re.sub(r"\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)", repl, md)


def _copy_solution_assets(solution_dir: Path, out_dir: Path) -> None:
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    for p in solution_dir.iterdir():
        if not p.is_file():
            continue
        if p.suffix.lower() not in IMAGE_EXTS:
            continue
        shutil.copy2(p, assets_dir / p.name)


def generate_one(solution_dir: Path) -> tuple[bool, str | None, str]:
    """
    Returns (ok, primary_category_or_none, page_title).
    """
    slug = solution_dir.name
    readme = solution_dir / "README.md"
    if not readme.exists():
        return False, None, ""

    raw = readme.read_text(encoding="utf-8", errors="replace")
    primary = _extract_primary_category(raw)
    title = _extract_h1_title(raw) or _slug_to_label(slug)

    md = raw
    md = _rewrite_solution_readme_links(md)
    md = _rewrite_local_image_links(md)

    out_dir = DOCS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.md").write_text(md, encoding="utf-8", newline="\n")
    _copy_solution_assets(solution_dir, out_dir)
    return True, primary, title


def main() -> None:
    if not SOLUTIONS_DIR.exists():
        raise SystemExit(f"Missing solutions dir: {SOLUTIONS_DIR}")
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    total = 0
    written = 0
    category_to_solutions: dict[str, list[tuple[str, str]]] = {}

    buckets: dict[str, list[tuple[str, str]]] = defaultdict(list)
    label_votes: dict[str, Counter[str]] = defaultdict(Counter)

    for d in sorted(SOLUTIONS_DIR.iterdir()):
        if not d.is_dir():
            continue
        total += 1
        ok, primary, title = generate_one(d)
        if ok:
            written += 1
            raw_label = primary.strip() if primary else "Uncategorized"
            key = _normalize_category_key(raw_label)
            buckets[key].append((d.name, title))
            label_votes[key][raw_label] += 1

    for key, pairs in buckets.items():
        display_name = label_votes[key].most_common(1)[0][0]
        category_to_solutions[display_name] = pairs

    _write_docs_index(category_to_solutions)
    _write_docs_pages_yml(category_to_solutions)

    print(f"Solutions scanned: {total}")
    print(f"Docs generated:   {written}")
    print(f"Categories:       {len(category_to_solutions)}")


if __name__ == "__main__":
    main()

