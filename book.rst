.. raw:: html

    <nav class="pagination-control">
        Generate page numbers for printing on
        <a href="?paginate=A4">A4 paper</a> /
        <a href="?paginate=Letter">U.S. Letter</a>
    </nav>

    <div class="megaheader">
    <img alt="GitFourchette logo" src="_static/gf.svg" width="64">
    <div>
        <div class="megaheader1">GitFourchette</div>
        <div class="megaheader2" style="text-align: left;">User&rsquo;s Guide</div>
    </div>
    </div>

    <div class="book-cover-page-footer">
    November 2024
    <br>&copy; 2024 Iliyas Jorio
    <br>https://gitfourchette.org
    </div>

    <nav id="single-page-toc">
    <h1>Contents</h1>
    <!-- filled in by script -->
    </nav>

..
    Sphinx won't output a TOC for single-page documents (https://github.com/sphinx-doc/sphinx/issues/1863)
    To get around this, we can replace toctree:: with contents:: + a bunch of include:: directives.
    However, this would break :doc: links in single-page mode!
    So instead I just use toctree here and generate the TOC in javascript.

.. toctree::
    :maxdepth: 2
    :caption: Contents
    :class: single-page-book-toctree

    guide/bookintro
    guide/newrepo
    guide/uitour
    guide/history
    guide/commit
    guide/changes
    guide/diff
    guide/branches
    guide/pullpush
    guide/remotes
    guide/advcommit
    guide/conflicts
    limitations