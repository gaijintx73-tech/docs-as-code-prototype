#!/usr/bin/env python3
"""Build the docs-as-code prototype site.

Reads every Markdown file in src/ and renders it to a matching HTML file
in this folder, using one shared template (site header + navigation).
Run it after editing any file in src/:

    python3 build.py

Requires the Python "markdown" package (pip install markdown).
"""
from pathlib import Path
import re

import markdown

BASE = Path(__file__).resolve().parent
SRC = BASE / "src"
SITE_TITLE = "Docs-as-Code Prototype"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site_title}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif;
         color: #1d2733; background: #f4f2ed; line-height: 1.65; }}
  header {{ background: #14456b; color: #fff; padding: 1.1rem 1.5rem; }}
  header .site {{ font-size: 1.35rem; font-weight: bold; letter-spacing: .02em; }}
  header .tag {{ font-size: .85rem; opacity: .85; font-style: italic; }}
  .wrap {{ display: flex; max-width: 1100px; margin: 0 auto; gap: 2rem;
           padding: 1.5rem 1rem 3rem; align-items: flex-start; }}
  nav {{ flex: 0 0 230px; background: #fff; border: 1px solid #ddd6c9;
         border-radius: 8px; padding: 1rem 1.1rem; position: sticky; top: 1rem; }}
  nav h2 {{ font-size: .8rem; text-transform: uppercase; letter-spacing: .08em;
           color: #6b7684; margin: 0 0 .6rem; }}
  nav ul {{ list-style: none; margin: 0; padding: 0; }}
  nav li {{ margin: .45rem 0; }}
  nav a {{ color: #14456b; text-decoration: none; font-size: .95rem; }}
  nav a:hover {{ text-decoration: underline; }}
  nav a.current {{ font-weight: bold; color: #b3541e; }}
  main {{ flex: 1; background: #fff; border: 1px solid #ddd6c9;
          border-radius: 8px; padding: 2rem 2.4rem; min-width: 0; }}
  main h1 {{ font-size: 1.7rem; line-height: 1.25; margin-top: 0; }}
  main h2 {{ font-size: 1.3rem; margin-top: 2rem; color: #14456b; }}
  main h3 {{ font-size: 1.1rem; margin-top: 1.6rem; }}
  main a {{ color: #14456b; }}
  blockquote {{ border-left: 3px solid #b3541e; margin-left: 0;
                padding-left: 1rem; color: #44515f; font-style: italic; }}
  footer {{ text-align: center; color: #6b7684; font-size: .85rem;
            padding: 0 1rem 2rem; }}
  @media (max-width: 760px) {{
    .wrap {{ flex-direction: column; }}
    nav {{ position: static; width: 100%; flex: none; }}
  }}
</style>
</head>
<body>
<header>
  <div class="site">{site_title}</div>
  <div class="tag">Prototype documentation site built from existing writing samples</div>
</header>
<div class="wrap">
  <nav>
    <h2>Pages</h2>
    <ul>
{nav}
    </ul>
  </nav>
  <main>
{body}
  </main>
</div>
<footer>Built from Markdown sources in the src folder with build.py.</footer>
</body>
</html>
"""


def page_title(md_text, fallback):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main():
    pages = []
    for md_file in sorted(SRC.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        pages.append({
            "stem": md_file.stem,
            "title": page_title(text, md_file.stem.replace("-", " ").title()),
            "text": text,
        })
    # Home page first, then the samples in file order
    pages.sort(key=lambda p: (p["stem"] != "index", p["stem"]))

    for page in pages:
        nav_items = []
        for other in pages:
            href = f"{other['stem']}.html"
            label = "Home" if other["stem"] == "index" else other["title"]
            cls = ' class="current"' if other["stem"] == page["stem"] else ""
            nav_items.append(f'      <li><a href="{href}"{cls}>{label}</a></li>')
        body = markdown.markdown(page["text"], extensions=["extra"])
        html = TEMPLATE.format(
            title=page["title"],
            site_title=SITE_TITLE,
            nav="\n".join(nav_items),
            body=body,
        )
        out = BASE / f"{page['stem']}.html"
        out.write_text(html, encoding="utf-8")
        print(f"built {out.name}  ({page['title']})")


if __name__ == "__main__":
    main()
