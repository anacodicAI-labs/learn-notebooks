#!/usr/bin/env python3
"""Execute a learn-hub companion notebook and render it to inline HTML.

Usage:
    python3 render_notebook.py ai-agents/6-1/what-are-agents.ipynb

What it does:
  1. Executes the notebook top-to-bottom (captures real outputs). Notebooks are
     designed to run WITHOUT an API key.
  2. Writes `<slug>.notebook.html` next to the matching article markdown in the
     site repo, which the article page then embeds inline
     (see lib/content.ts getLearnArticleNotebookHtml).

This repo holds the notebook SOURCES; the site repo holds the articles. The two
are separate repositories, so the output location is resolved as:

    $LEARN_TUTORIALS_DIR                                  if set, else
    ../anacodic.ai-labs/s3-content/learn/tutorials         (sibling checkout)

Notes:
  - Uses the nbclient/nbconvert Python API directly to bypass a broken
    jupyter_contrib_nbextensions in some environments (the `jupyter nbconvert`
    CLI crashes on import there).
  - Notebooks are laid out as <module>/<sub>/<slug>.ipynb so the output path
    mirrors the article tree exactly.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from traitlets.config import Config

NOTEBOOKS_DIR = Path(__file__).resolve().parent             # this repo's root
_DEFAULT_TUTORIALS = (
    NOTEBOOKS_DIR.parent / "anacodic.ai-labs" / "s3-content" / "learn" / "tutorials"
)
TUTORIALS_DIR = Path(
    os.environ.get("LEARN_TUTORIALS_DIR") or _DEFAULT_TUTORIALS
).resolve()

# Fail loudly rather than silently writing renders somewhere nothing reads them.
if not TUTORIALS_DIR.is_dir():
    sys.exit(
        f"article tree not found: {TUTORIALS_DIR}\n"
        "Either check out the site repo as a sibling of this one, or point at it:\n"
        "  LEARN_TUTORIALS_DIR=/path/to/s3-content/learn/tutorials "
        "python3 render_notebook.py <module>/<sub>/<slug>.ipynb"
    )


def render(nb_rel_path: str) -> Path:
    # Accept both "notebooks/<module>/<sub>/<slug>.ipynb" and "<module>/<sub>/<slug>.ipynb";
    # either way it resolves against this repo's root. The leading "notebooks/" is
    # tolerated for paths copied from the old single-repo layout.
    rel = nb_rel_path[len("notebooks/"):] if nb_rel_path.startswith("notebooks/") else nb_rel_path
    nb_path = (NOTEBOOKS_DIR / rel).resolve()
    if not nb_path.exists():
        sys.exit(f"notebook not found: {nb_path}")

    # <module>/<sub>/<slug>.ipynb
    #   -> <tutorials>/<module>/<sub>/<slug>.notebook.html   (beside the article)
    parts = nb_path.relative_to(NOTEBOOKS_DIR).parts
    module, sub, filename = parts[-3], parts[-2], parts[-1]
    slug = filename[:-6]  # strip .ipynb
    out_dir = TUTORIALS_DIR / module / sub
    out_dir.mkdir(parents=True, exist_ok=True)
    out_html = out_dir / f"{slug}.notebook.html"

    nb = nbformat.read(str(nb_path), as_version=4)
    print(f"executing {nb_path.name} ...")
    NotebookClient(nb, timeout=180, kernel_name="python3").execute()
    nbformat.write(nb, str(nb_path))  # persist captured outputs back into the source

    exporter = HTMLExporter(config=Config(), template_name="lab")
    exporter.preprocessors = []
    body, _ = exporter.from_notebook_node(nb)
    out_html.write_text(body)
    print(f"rendered -> {out_html}  ({len(body)} bytes)")
    return out_html


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    # Isolate from a broken user jupyter config dir if present.
    os.environ.setdefault("JUPYTER_CONFIG_DIR", "/tmp/_empty_jupyter_cfg")
    Path(os.environ["JUPYTER_CONFIG_DIR"]).mkdir(parents=True, exist_ok=True)
    render(sys.argv[1])
