# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme
# -- Project information

project = u'Motif HxH'
copyright = u'2023, Layla Hirsh'
author = u'Layla Hirsh'


html_theme = "sphinx_rtd_theme"
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
