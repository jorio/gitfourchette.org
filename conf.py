import sys, os

# print("TAGS", tags)
BOOK_FILES = ['book.rst', 'guide/bookintro.rst']
NONBOOK_FILES = ['index.rst', 'guide/index.rst', 'install.rst']

# -----------------------------------------------------------------------------
# Project information

project = 'GitFourchette'
copyright = '%Y Iliyas Jorio'
author = 'Iliyas Jorio'
version = "1.0.0"

# -----------------------------------------------------------------------------
# General configuration

nitpicky = True

templates_path = []

exclude_patterns = ['_build', 'snippets', 'Thumbs.db', '.DS_Store']
exclude_patterns += BOOK_FILES

# For directives.py:
sys.path.append(os.path.abspath("."))
extensions = [
    'directives',
]

rst_prolog = """
.. include:: /snippets/prolog.rst
"""

#ogp_site_url = 'https://gitfourchette.org'
#ogp_image = '_static/ogp_image.png'

# -----------------------------------------------------------------------------
# html

html_logo = "assets/gf.svg"
html_favicon = "assets/gf.svg"
# html_last_updated_fmt = "%c"
html_title = project
html_show_sourcelink = False
html_copy_source = False

html_static_path = ['_static']
html_js_files = ['gitfourchette.js']
html_css_files = ['gitfourchette.css', ('gitfourchette-print.css', {'media': 'print'})]

html_theme = 'furo'

# -----------------------------------------------------------------------------
# singlehtml

if any(arg in ['singlehtml', 'epub'] for arg in sys.argv):
    master_doc = 'book'
    html_title = f'{project} User&rsquo;s Guide'
    html_theme = 'basic'
    html_theme_options = {'nosidebar': True,}
    html_css_files = ['gitfourchette.css', 'gitfourchette-print.css']
    html_js_files.append('gitfourchette-book.js')
    templates_path.append("_booktemplates")
    exclude_patterns = list(set(exclude_patterns) - set(BOOK_FILES)) + NONBOOK_FILES
