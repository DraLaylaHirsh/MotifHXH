"""
Shared Sphinx configuration using sphinx-multiproject.

To build each project, the ``PROJECT`` environment variable is used.

.. code:: console

   $ make html  # build default project
   $ PROJECT=dev make html  # build the dev project

for more information read https://sphinx-multiproject.readthedocs.io/.
"""

import os
import sys
import sphinx_rtd_theme
master_doc = "index"
copyright = "Read the Docs, Inc & contributors"
version = "10.1.0"
release = version
 

# Intersphinx: Do not try to resolve unresolved labels that aren't explicitly prefixed.
# The default setting for intersphinx_disabled_reftypes can cause some pretty bad
# breakage because we have rtd and rtd-dev stable versions in our mappings.
# Hence, if we refactor labels, we won't see broken references, since the
# currently active stable mapping keeps resolving.
# Recommending doing this on all projects with Intersphinx.
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]
 
language = "en"

locale_dirs = [
    f"{docset}/locale/",
]
gettext_compact = False

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static", f"{docset}/_static"]
html_css_files = ["css/custom.css", "css/sphinx_prompt_css.css"]
html_js_files = ["js/expand_tabs.js"]




