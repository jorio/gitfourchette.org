Limitations
===========

Supported operating systems
---------------------------

|App| is built primarily for Linux and it fits in great with KDE Plasma. It will
also work fine on macOS.

I don't have time to support Windows. |App| does start from source on Windows,
but some important features will not work.

libgit2 mode, Vanilla git mode
------------------------------

By default, |App| manipulates Git repositories with `libgit2 <https://libgit2.org>`_ (via `pygit2 <https://www.pygit2.org>`_). This is a standalone implementation of Git's core methods which is separate from the ``git`` program itself.

:gfversion:`New in v1.5.0:` You can now choose to carry out most tasks via your system's ``git`` instead of libgit2. You may benefit from this if your workflow isn't supported in libgit2 mode: in particular, if you depend on a custom OpenSSH configuration or your repo has custom hooks.

To switch between "libgit2" and "vanilla git" modes, go to |cogwheel| :menuselection:`Settings --> Advanced`, then change the **Preferred Git backend** option:

.. figure:: /assets/screens/gitbackend.png

Git version 2.41 or later is recommended for best results in vanilla git mode.

The vanilla git mode is still experimental. It may become the default in a future release depending on user feedback. You're welcome to try it out and report any issues with it.


Missing features
----------------

**Not implemented yet** ---
Support for these features may be implemented eventually, depending on demand,
funding, and how much free time I can carve out for the project.

- Rebase
- LFS
