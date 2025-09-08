import sys, os

# print("TAGS", tags)
BOOK_FILES = ['book.rst', 'guide/bookintro.rst']
NONBOOK_FILES = ['index.rst', 'guide/index.rst', 'install.rst']

# -----------------------------------------------------------------------------
# Project information

project = 'GitFourchette'
copyright = '%Y Iliyas Jorio'
author = 'Iliyas Jorio'
version = "1.5.0"
revdate = "September 2025"

html_context = {
    "revdate": revdate,
    "revyear": revdate.split()[-1],
}

# -----------------------------------------------------------------------------
# General configuration

nitpicky = True

templates_path = ["_templates"]

exclude_patterns = ['_build', 'snippets', 'Thumbs.db', '.DS_Store']
exclude_patterns += BOOK_FILES

# For directives.py:
sys.path.append(os.path.abspath("."))
extensions = [
    'directives',
    'myst_parser',  # for markdown support (CHANGELOG)
]

rst_prolog = """
.. include:: /snippets/prolog.rst
"""

for k, v in html_context.items():
    rst_prolog += f".. |{k}| replace:: {v}\n"

#ogp_site_url = 'https://gitfourchette.org'
#ogp_image = '_static/ogp_image.png'

# -----------------------------------------------------------------------------
# html

html_logo = "assets/gf.svg"
html_favicon = "assets/gf.svg"
# html_last_updated_fmt = "%c"
html_title = project
html_copy_source = False

html_extra_path = ['_extra']  # deploy raw files to HTML output
html_static_path = ['_static']
html_js_files = ['gitfourchette.js']
html_css_files = ['gitfourchette.css', ('gitfourchette-print.css', {'media': 'print'})]

html_theme = 'furo'

html_theme_options = {
    "source_repository": "https://github.com/jorio/gitfourchette.org",
    "source_branch": "sphinx",
    "top_of_page_buttons": ["view"],
}

# Modified from https://pradyunsg.me/furo/customisation/sidebar/#default-design
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/gitfourchette-current-version.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

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
