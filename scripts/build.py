"""Build a dependency-free HTML report from the checked-in practicals."""
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]
def render():
    sections = []
    for path in sorted((ROOT / 'practicals').glob('P*.md')):
        sections.append('<section><pre>' + escape(path.read_text()) + '</pre></section>')
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Git Lab · 0064</title><style>body{max-width:960px;margin:40px auto;padding:24px;font:16px system-ui;background:#f4f6fb;color:#17243c}section{background:white;padding:24px;margin:24px 0;border-radius:12px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.7 monospace}</style><h1>Git &amp; GitHub practicals</h1><p>Abhinav Bansal · 0064 · BCA-AI</p>' + ''.join(sections) + '</html>'
if __name__ == '__main__':
    (ROOT / 'site').mkdir(exist_ok=True)
    (ROOT / 'site/index.html').write_text(render())
