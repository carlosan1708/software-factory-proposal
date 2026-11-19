"""Export both website reading modes to the static download directory."""

import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

from playwright.sync_api import sync_playwright


SITE = Path(__file__).resolve().parents[1] / "site"
ORIGIN = "https://software-factory-proposal.web.app"


def export(channel):
    destination = SITE / "downloads"
    destination.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=destination.parent.parent) as temp, sync_playwright() as pw:
        browser = pw.chromium.launch(channel=channel)
        for mode in ("executive", "technical"):
            page = browser.new_page(reduced_motion="reduce")
            # Render the local revision with canonical URLs for links in the document.
            url = ORIGIN + ("/technical" if mode == "technical" else "/")
            page.route(url, lambda route: route.fulfill(path=SITE / "index.html", content_type="text/html"))
            page.goto(url)
            page.wait_for_selector(f"#{mode}:checked", state="attached")
            page.emulate_media(media="print")
            # Follow the scenario selector's Phase 1 / Phase 2 reading order.
            page.evaluate("""() => {
                const scene = document.querySelector('.run-scene');
                for (const input of document.querySelectorAll('input[name="scenario"]'))
                    scene.before(document.querySelector('[data-case="' + input.value + '"]'));
                for (const question of document.querySelectorAll('#faq details'))
                    question.open = true;
            }""")
            title = "Software Factory on Azure · " + mode.title()
            page.evaluate("(title) => document.title = title", title)
            footer = (
                '<div style="font:9px Arial;color:#555;width:100%;margin:0 15mm;'
                'display:flex;justify-content:space-between"><span>' + title + '</span>'
                '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
            )
            page.pdf(path=Path(temp) / f"software-factory-{mode}.pdf",
                     prefer_css_page_size=True, print_background=True, tagged=True,
                     outline=True, display_header_footer=True, header_template="<span></span>",
                     footer_template=footer)
            page.close()
        browser.close()
        for pdf in sorted(Path(temp).glob("*.pdf")):
            pdf.replace(destination / pdf.name)
            print(destination / pdf.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", help="Installed Chromium channel, e.g. chrome or msedge.")
    export(parser.parse_args().channel)
