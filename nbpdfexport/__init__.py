#!/usr/bin/env python3
"""
Generate PDF with cells with just given tag.

I can never figure out nbconvert's API, unfortunately.
"""
import argparse
import nbconvert
import tempfile
import asyncio
import tempfile
from pyppeteer import launch


async def html_to_pdf(html_file, pdf_file):
    """
    Convert arbitrary HTML file to PDF
    """
    browser = await launch()
    page = await browser.newPage()
    await page.goto(f'file:///{html_file}')
    await page.pdf({'path': pdf_file})
    await browser.close()


def notebook_to_pdf(notebook_path, pdf_path):
    """
    Convert given notebook file to PDF
    """
    exporter = nbconvert.HTMLExporter(config={})
    exported_html, _ = exporter.from_filename(notebook_path)

    with tempfile.NamedTemporaryFile(suffix='.html') as f:
        f.write(exported_html.encode())
        f.flush()
        asyncio.get_event_loop().run_until_complete(html_to_pdf(f.name, pdf_path))

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'notebook_path',
        help='Path to .ipynb file to convert'
    )
    argparser.add_argument(
        'pdf_path',
        help='Path to output PDF file to'
    )

    args = argparser.parse_args()

    notebook_to_pdf(args.notebook_path, args.pdf_path)

if __name__ == '__main__':
    main()