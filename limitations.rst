Limitations
===========

Supported operating systems
---------------------------

|App| is built primarily for Linux and it fits in great with KDE Plasma. It will
also work fine on macOS.

I don't have time to support Windows. |App| does start from source on Windows,
but some important features will not work---in particular, network operations on
SSH remotes.

|App| doesn't depend on ``git``
-------------------------------

|App| doesn't need Git to be installed on your system---it doesn't actually
talk to the ``git`` program itself.
It's based on `libgit2 <https://libgit2.org>`_ (via `pygit2 <https://pygit2.org>`_),
which is a standalone implementation of Git's core methods.
This makes |App| completely independent from your ``git`` install.

Since |App| and ``git`` are completely separate programs,
you may notice some minor differences between |App|'s behavior
and vanilla Git's. Feel free to report an issue if any
unexpected discrepancies come up.

Missing features
----------------

**On my roadmap** ---
|App| is still under development; some Git features are not supported yet. I
plan to support these in the near future, or I may be actively working on them:

- File blame
- File history

**Not implemented yet** ---
Support for these features may be implemented eventually, depending on demand,
funding, and how much free time I can carve out for the project.

- Rebase
- LFS
- Hooks
- Syntax highlighting in diff view
