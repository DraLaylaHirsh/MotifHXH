# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme
# -- Project information

project = u'Motif HxH'
copyright = u'2023, Layla Hirsh'
author = u'Layla Hirsh'

sphinx==5.3.0
sphinx_rtd_theme==1.1.1
readthedocs-sphinx-search==0.1.1


release = '1'
version = '1.0'

html_theme = "sphinx_rtd_theme"
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]


intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

latex_logo =  'REFRACT.png'
# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

