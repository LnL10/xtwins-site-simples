"""Gera requirements/requisitos-gestor-tarefas.pdf a partir do .md.

Uso: pip install markdown playwright && playwright install chromium
     python tools/build_pdf.py
"""

from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

SOURCE = Path(__file__).resolve().parent.parent / "requirements" / "requisitos-gestor-tarefas.md"

STYLE = """
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #222; }
h1 { font-size: 19pt; color: #1e3a8a; margin: 0 0 4pt; }
h2 { font-size: 13.5pt; margin-top: 16pt; border-bottom: 1px solid #ddd; padding-bottom: 3pt; }
table { border-collapse: collapse; margin: 6pt 0; }
td, th { border: 1px solid #999; padding: 3pt 7pt; text-align: left; vertical-align: top; }
th { background: #eef2ff; }
code { font-family: Consolas, monospace; }
"""


def main():
    body = markdown.markdown(SOURCE.read_text(encoding="utf-8"), extensions=["tables"])
    html = f'<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><style>{STYLE}</style></head><body>{body}</body></html>'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.pdf(path=str(SOURCE.with_suffix(".pdf")), format="A4",
                 margin={"top": "18mm", "bottom": "18mm", "left": "17mm", "right": "17mm"},
                 display_header_footer=True, header_template="<span></span>",
                 footer_template='<div style="font-size:8pt;width:100%;text-align:center;color:#888">Gestor de Tarefas · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
        browser.close()
    print("ok", SOURCE.with_suffix(".pdf").name)


if __name__ == "__main__":
    main()
