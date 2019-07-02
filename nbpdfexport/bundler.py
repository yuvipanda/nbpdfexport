"""
Bundler Extension for classic Jupyter Notebook
"""
import os
from . import notebook_to_pdf
import tempfile
import nbformat
import json

async def bundle(handler, model):
    """
    """
    # uh, sometimes model doesn't have a metadata field and so we can't make a notebooknode?
    with tempfile.TemporaryDirectory() as d:
        pdf_path = os.path.join(d, 'output.pdf')
        await notebook_to_pdf(model['content'], pdf_path)

        # FIXME: Optimize this streaming somehow?
        handler.set_header('Content-Type', 'application/pdf')
        handler.set_header('Content-Length', os.path.getsize(pdf_path))
        # Mark this as a 'download' action
        download_filename = os.path.splitext(model['name'])[0] + '.pdf'
        handler.set_header('Content-Disposition', 'attachment; filename={}'.format(download_filename))

        with open(pdf_path, mode='rb') as f:
            handler.write(f.read())
        handler.finish()


def _jupyter_bundlerextension_paths():
    """
    Entrypoint for Jupyter Notebook Bundler

    Shows up in the 'Download' menu on Jupyter Classic Notebook
    """
    return [{
        'name': 'chrome_pdf_export',
        'label': 'PDF via Chrome (.pdf)',
        'module_name': 'nbpdfexport.bundler',
        'group': 'download'
    }]