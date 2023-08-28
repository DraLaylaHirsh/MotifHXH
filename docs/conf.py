# Configuration file for the Sphinx documentation builder.

# -- Project information

project = u'Motif HxH'
copyright = u'2023, Layla Hirsh'
author = u'Layla Hirsh'


html_theme = 'sphinx_rtd_theme'
extensions = [
+    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints'
]
