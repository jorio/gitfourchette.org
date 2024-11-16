Managing the Uncommitted Changes
================================

This chapter will teach you some techniques to manage and edit your uncommitted
changes so you can prepare commits with more precision.  We'll assume you're
already familiar with staging and unstaging files (see :doc:`commit`).

Staging and discarding individual hunks or lines
------------------------------------------------

Sometimes, you might be ready to commit specific parts of a file---but you might
still be working on other parts of that file.

Fortunately, you don't have to stage the entire file every time you want to make
a commit.  The :doc:`Diff View <diff>` lets you stage small pieces of code in a
file:

- You can :ref:`stage a single hunk <diff-hunk-tools>` without staging the full file.
- You can even :ref:`stage individual lines <diff-line-tools>` if a hunk isn't granular enough.

.. figure:: /assets/screens/diffselection.png

    Hand-picked lines ready to be staged in the Diff View.

.. _stash-changes:

Stashing changes
----------------

If your working directory contains changes that you're not ready to commit yet,
you can **stash** them.  *Stashing* safely tucks away your changes to a *stash*,
then it restores the affected files to their unchanged state. When you're ready
to resume working on the stashed changes, you can *apply the stash* back to your
working directory.

This is handy when you want to reset your working directory to a clean slate
without losing work in progress.

To create a stash, go to :menuselection:`Repo --> Stash Changes`;
or, select some files in the File List, right-click and choose :guilabel:`Stash Changes`.
This opens the "New Stash" dialog where you can customize the contents
of the stash before confirming:

.. figure:: /assets/screens/newstash.png

    The New Stash dialog.

.. list-table:: Fields in the New Stash dialog
    :header-rows: 1
    :widths: 25 75

    * - Item
      - Description

    * - Optional stash message
      - Describe the contents of your stash here. Or not---it's up to you.
        Stashes are meant to be temporary, so this message is optional.

    * - Retain stashed changes in working directory
      - Unticked by default, since the most common use case for stashes is
        to set aside some work in progress and clean up your working directory.
        Tick this if you want to stash the changes and keep them in your
        working directory anyway.

    * - Files to stash
      - Select the files to include in the stash.
        Unticked files will not be part of the stash and will remain in your
        working directory.

Your new :gficon:`git-stash` stash appears in the Sidebar's :guilabel:`Stashes`
section.  To restore a stash to your working directory, right-click on it in the
Sidebar and choose :guilabel:`Apply`.

.. warning::
    If you stash a file that contains **both staged and unstaged** changes,
    those will be "flattened" in the stash.

.. note::
    Stashes are only saved locally on your machine.
    They cannot be shared with others (unlike "shelves" in Perforce).

.. tip::
    Press :kbd:`Ctrl Alt S` to create a new stash.

.. _rescue-changes:

Rescuing changes that you discarded by mistake
----------------------------------------------

Did you mistakenly :gficonlabel:`git-discard Discard` some change
that you actually meant to keep?

Don't panic---|App| backs up the last 250 discarded changes by default. Go to
:menuselection:`Help --> Open Trash` and your system's file manager will reveal
the trash folder.

In the trash, discarded changes are stored as `.patch` files that you can apply
to your working directory. To do so, drag-and-drop a patch file from your file
manager to |App|'s main window.

Applying the patch might fail if your working directory has evolved too much. In
this case, try applying the patch with `git apply` (unfortunately, |App|'s
patcher is a bit brittle for now and vanilla `git apply` is more robust).

.. note:: You can customize how many files to keep in the trash in |cogwheel| :menuselection:`Settings --> Trash`.

.. _uc-files-cm:

File List context menu (in Uncommitted Changes)
-----------------------------------------------

The Stage/Unstage/Discard buttons around the file lists should cover most of
your basic staging needs.

|rmb| Right-click on a file in one of the File Lists to open a context menu with advanced operations:

.. list-table:: Actions in the File List context menu (from Uncommitted Changes)
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - Stage File
      - Stage all changes in the selected file.

    * - Unstage File
      - Unstage all changes in the selected file.

    * - Discard Changes
      - Discard the changes in the selected files. Your working copy of the file
        will be identical to the state of the file on the HEAD commit.

    * - Stash Changes
      - Save the changes in the selected file to a "stash",
        then (optionally) revert the file to its unmodified state.
        See :ref:`stash-changes`.

    * - Revert Mode Change
      - If this file's mode has changed (most commonly, the executable bit "+x"),
        you can use this command to restore the previous mode.

    * - Open Diff In...
      - Open this diff in an external program.
        Set up the external diff tool in
        |cogwheel| :menuselection:`Settings --> External Tools`.

    * - Export Diff As Patch
      - Save this change as a "unified diff" patch file.

    * - Edit In...
      - Edit the working copy of this file in an external program.
        Set up the external editor in
        |cogwheel| :menuselection:`Settings --> External Tools`.

    * - Edit HEAD Version In...
      - View the "unmodified" revision of this file (as of the HEAD commit)
        in an external program. Set up the external editor in
        |cogwheel| :menuselection:`Settings --> External Tools`.

    * - Open Folder
      - Reveal this file in your system's file manager.

    * - Copy Path
      - Copy the absolute path to this file to the clipboard.
