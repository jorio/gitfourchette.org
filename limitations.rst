Limitations
===========

Supported operating systems
---------------------------

|App| is built primarily for Linux and it fits in great with KDE Plasma.
It also runs fine on macOS, but Linux remains the primary target and
there's no official Mac support (yet).

I don't have time to support Windows. |App| does start from source on Windows,
but some important features will not work.

Tentative feature roadmap
-------------------------

Support for these features may be implemented eventually, depending on demand,
funding, and how much free time I can carve out for the project:

- Rebase
- Improved LFS support

Improved compatibility with vanilla Git since v1.5.0
----------------------------------------------------

:gfversion:`New in v1.5.0.` Starting with v1.5.0, |App| now uses Git itself to
edit repositories and communicate with remotes. This improves compatibility
with workflows that depend on OpenSSH, hooks, etc.

For performance, |App| still uses libgit2 to build its model of the repository,
but all operations that write to the repo or use the network now use Git directly.

The Flatpak version uses an embedded Git distribution by default. You can switch
to another Git instance via |cogwheel| :menuselection:`Settings --> Git
Integration`.
