# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme
# -- Project information

project = u'Motif HxH'
copyright = u'2023, Layla Hirsh'
author = u'Layla Hirsh'




extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_rtd_theme',
]
...
html_theme = 'sphinx_rtd_theme'
