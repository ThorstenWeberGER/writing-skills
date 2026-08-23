"""Generate a LinkedIn carousel PDF from the Caught Clean visual system.

Renders each slide as HTML/canvas at 1080x1350px (LinkedIn's 4:5 page size),
screenshots it with a headless browser, then assembles the screenshots into
one PDF. See styleguide.html for the palette, type and layout rules this
script implements, and README.md for how to write a new deck.
"""
import argparse
import glob
import os
import pathlib

import img2pdf
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).parent
TEMPLATE = (BASE / "slide_template.html").read_text()

# Named palettes from styleguide.html's "Color variants" section.
# Each is (wash-a rgb, wash-b rgb) in "r,g,b" string form.
PALETTES = {
    "sage_blush": ("148,178,166", "227,178,166"),
    "slate_ochre": ("159,176,194", "227,196,138"),
    "moss_clay": ("168,181,140", "209,156,124"),
    "lilac_sand": ("183,168,201", "228,207,174"),
}

# Named compositions from styleguide.html's "Background variants" section.
def wash_js(composition, a, b):
    if composition == "corner":
        return f"""
        wash(ctx, w*0.18, h*0.86, w*0.34, h*0.28, '{a}', 0.55, 1);
        wash(ctx, w*0.14, h*0.1, w*0.32, h*0.24, '{b}', 0.5, 6);
        """
    if composition == "horizon":
        return f"""
        wash(ctx, w*0.5, h*0.92, w*0.62, h*0.14, '{a}', 0.5, 2);
        wash(ctx, w*0.5, h*0.85, w*0.4, h*0.09, '{b}', 0.32, 5);
        """
    if composition == "scatter":
        return f"""
        wash(ctx, w*0.16, h*0.12, w*0.16, h*0.11, '{a}', 0.5, 1);
        wash(ctx, w*0.82, h*0.1, w*0.13, h*0.09, '{b}', 0.42, 3);
        """
    # "both": corner composition with both washes at reduced opacity,
    # reserved for a deck's closing slide.
    return f"""
    wash(ctx, w*0.18, h*0.86, w*0.34, h*0.28, '{a}', 0.4, 1);
    wash(ctx, w*0.22, h*0.9, w*0.3, h*0.24, '{a}', 0.25, 6);
    wash(ctx, w*0.14, h*0.1, w*0.5, h*0.4, '{b}', 0.35, 2);
    wash(ctx, w*0.2, h*0.16, w*0.28, h*0.22, '{b}', 0.22, 5);
    """

# The example deck: "Caught Clean", the writing-skill article's pyramid
# (the failure, the stake, the fix) mapped onto three slides. Edit this
# list, or replace it, to build a new deck; each entry's "wash" picks a
# composition ("corner" | "horizon" | "scatter" | "both") for that slide.
SLIDES = [
    {
        "wash": "corner",
        "content": """
        <div class="kicker">The failure</div>
        <div class="headline" style="font-size:112px; line-height:1.08;">It reported<br>the draft<br>clean.</div>
        <div class="caption-block">
          <div class="caption">The em dash was still in the client's inbox.</div>
          <div class="foot"><span class="num">01</span><span>Swipe &rarr;</span></div>
        </div>
        """,
    },
    {
        "wash": "corner",
        "content": """
        <div class="kicker">The stake</div>
        <div class="headline" style="font-size:94px; line-height:1.14;">Readers notice<br>the AI draft<br>before you do.</div>
        <div class="caption-block">
          <div class="caption" style="max-width:17ch;">A client, a boss, a hiring manager, the one reader you can't afford to lose.</div>
          <div class="foot"><span class="num">02</span><span>Swipe &rarr;</span></div>
        </div>
        """,
    },
    {
        "wash": "both",
        "content": """
        <div class="kicker">The fix</div>
        <div class="headline" style="font-size:100px; line-height:1.1;">Now it checks<br>itself. 26 rules,<br>before you post.</div>
        <div class="caption-block">
          <svg width="180" height="40" viewBox="0 0 64 14" fill="none"><path d="M2 9.5C14 4 24 11.5 33 7C42 2.5 52 9 62 5.5" stroke="#8a5a44" stroke-width="2.2" stroke-linecap="round"/></svg>
          <div class="caption">Free skill for Claude. Drafts, checks, names the rule behind every flag.</div>
        </div>
        """,
    },
]


def find_chromium():
    """Locate a Chromium binary Playwright can launch.

    Falls back to a manual search under PLAYWRIGHT_BROWSERS_PATH when the
    installed `playwright` package expects a browser revision newer than
    the one actually on disk (a version-pin mismatch, not a missing
    install).
    """
    browsers_path = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
    for root in [browsers_path, os.path.expanduser("~/.cache/ms-playwright")]:
        if not root:
            continue
        for candidate in glob.glob(os.path.join(root, "chromium*", "chrome-linux", "chrome")):
            return candidate
    return None


def build(palette_name, out_path):
    a, b = PALETTES[palette_name]
    out_path = pathlib.Path(out_path).resolve()
    work_dir = out_path.parent
    work_dir.mkdir(parents=True, exist_ok=True)

    html_paths = []
    for i, s in enumerate(SLIDES, start=1):
        html = TEMPLATE.replace("__CONTENT__", s["content"]).replace(
            "__WASH__", wash_js(s["wash"], a, b)
        )
        hp = work_dir / f"slide{i}.html"
        hp.write_text(html)
        html_paths.append(hp)

    png_paths = []
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            chromium = find_chromium()
            if not chromium:
                raise
            browser = p.chromium.launch(executable_path=chromium)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for i, hp in enumerate(html_paths, start=1):
            page.goto(hp.as_uri())
            page.wait_for_timeout(400)  # let the webfont and canvas paint settle
            pp = work_dir / f"slide{i}.png"
            page.screenshot(path=str(pp))
            png_paths.append(pp)
        browser.close()

    pdf_bytes = img2pdf.convert([str(p) for p in png_paths])
    out_path.write_bytes(pdf_bytes)
    print(f"wrote {out_path} ({out_path.stat().st_size:,} bytes, {len(png_paths)} pages)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--palette", choices=sorted(PALETTES), default="sage_blush",
        help="color variant from styleguide.html (default: sage_blush)",
    )
    parser.add_argument(
        "--out", default=str(BASE / "output" / "carousel.pdf"),
        help="output PDF path (default: output/carousel.pdf)",
    )
    args = parser.parse_args()
    build(args.palette, args.out)
