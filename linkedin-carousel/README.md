# LinkedIn carousel: Caught Clean

A visual system for LinkedIn carousel PDFs, plus the script that renders one.

## Files

- **`styleguide.html`** — the design system: palette, type, layout, watercolor wash technique, background and color variants, LinkedIn's platform rules, and the content formula for mapping an article's pyramid onto three slides. Open it in a browser. Read this before building a new deck.
- **`slide_template.html`** — the HTML/CSS/canvas template one slide renders from, at a fixed 1080x1350px (LinkedIn's 4:5 page size).
- **`build.py`** — renders each slide in `SLIDES` (inside `build.py`) with a headless browser, screenshots it, and assembles the screenshots into one multi-page PDF.

## Requirements

```
pip install playwright img2pdf
```

A Chromium binary reachable by Playwright. `build.py` tries the default Playwright install first, then falls back to searching `$PLAYWRIGHT_BROWSERS_PATH` for a `chromium*/chrome-linux/chrome` binary, which covers environments where a pre-installed browser's revision doesn't match the installed `playwright` package's expected version.

## Usage

```
python3 build.py
```

Writes `output/carousel.pdf`: 3 pages, 1080x1350px, using the default `sage_blush` palette and the deck defined in `SLIDES`.

Options:

```
python3 build.py --palette slate_ochre --out output/my-deck.pdf
```

- `--palette`: one of `sage_blush` (default), `slate_ochre`, `moss_clay`, `lilac_sand` — see styleguide.html's "Color variants" for which topic each fits.
- `--out`: output PDF path. The parent directory is created if needed.

## Building a new deck

1. Read `styleguide.html`'s "Content formula" section: slide 1 is the hook (the article's opening fact), slide 2 is the reader's stake (who pays and what it costs them), slide 3 is the resolution (the fix, plus one line the reader can act on).
2. Edit the `SLIDES` list in `build.py`. Each entry has a `wash` (`"corner"`, `"horizon"`, `"scatter"`, or `"both"` for a closing slide) and `content` (the kicker, headline, caption and page-number markup for that slide).
3. Keep every slide's wash on the same composition, per styleguide.html's rule against mixing compositions within one deck.
4. Never place text, the page-number marker, or a wash in the bottom-right corner. LinkedIn overlays its own page counter and zoom control there on every page.
5. Run `python3 build.py` and check the PDF before uploading: 3 slides is intentionally short for a tight pyramid, but LinkedIn's own data favors 5-15 pages for a longer deck.

## LinkedIn's carousel spec

Enforced by this system's fixed 1080x1350px canvas and the bottom-right safe zone in `slide_template.html`; see `styleguide.html`'s "Platform rules" section for the full list (PDF format, under 100 MB, 2-300 pages).
