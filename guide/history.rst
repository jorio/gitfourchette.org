Exploring the Commit History
============================

The Commit History displays a list of commits in the repository, along with a graph to visualize how the branches evolve.

You can |lmb|  left-click on any commit to
:ref:`explore its contents <explore-commit>`,
or |rmb|  :ref:`right-click to perform an action with the commit <history-cm>`.

.. tip::
    Press :kbd:`Alt 2` to get keyboard focus on the Commit History.

.. _history-101:

Overview of the Commit History
------------------------------

.. _figure-commithistory:
.. figure:: /assets/screens/commithistory.png

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", () => addFigurePins(
            "#figure-commithistory",
            {x:05, y:48, title:'Hash'},
            {x:12, y:84, title:'Graph'},
            {x:25, y:27, title:'Ref Boxes'},
            {x:40, y:60, title:'Commit Summary'},
            {x:75, y:40, title:'Author Name & Date'},
            {x:80, y:03, title:'Search Bar'},
        ));
    </script>

1. **Hash:** The first few characters of the commit's SHA-1 hash. It uniquely identifies the commit.
2. **Graph:** A visualization of the branches at this point in history. The dot represents the commit itself.
3. **Ref Boxes:** Colored boxes shown for each **reference** to this commit by:
    - The tip of a local branch, in purple, e.g. :gfinline:`/assets/screens/refbox-lb.png`
    - The tip of a remote branch, in blue-green, e.g. :gfinline:`/assets/screens/refbox-rb.png`
    - Tags, in yellow, e.g. :gfinline:`/assets/screens/refbox-tag.png`
4. **Commit Summary:** The first line of the commit message. An ellipsis (|ellip|) indicates that the message is truncated; hover over it to reveal the full message in a tooltip.
5. **Author Name/Date:** Who created the commit and when. See :ref:`author-vs-committer`.
6. **Search Bar:** See :ref:`find-commit`.

.. note::
    You can customize the appearance of some of these items in
    |cogwheel| :menuselection:`Settings --> Commit History`.
    For example, you can tweak:

    - Author column: full name, last name only, initials, email, etc.;
    - Date/time formats: ISO, U.S., European, etc.;
    - Row spacing and alternating background color...

.. _author-vs-committer:

Author vs. Committer
--------------------

The Commit History displays information about a commit's **author:** their name and the date at which they made the commit. But in some cases, a commit might have been revised by someone else than the original author---this person is called the **committer**.

An **asterisk (\*)** appears after the author's name and/or date if they differ from the committer's for any given commit.

.. note::
    You can always hover over the author's name or date to reveal a tooltip with details about the people involved in making the commit.

    .. figure:: /assets/screens/authortooltip.png

        Sample tooltip where the author (top) and committer (bottom) are distinct people.

Timestamps displayed in the Commit History are relative to your **local time**. The author/committer tooltip (see above) shows the original **timezones**.

.. _find-commit:

Finding a commit
----------------

The Commit History has a :gficon:`magnifying-glass` **Search Bar**.
Press :kbd:`Ctrl F` to invoke it (the Commit History must have keyboard focus).
Start typing, and a yellow highlight will appear in matching commits.

.. figure:: /assets/screens/searchword.png

    Searching for a word in the Commit History.

You can search for:

- The first couple characters of a commit's **SHA-1 hash**.
- Any part of a **commit message**. If the search term is found beyond the first line of the message, the ellipsis (|ellip|) will be highlighted in yellow.
- A commit's **author name**.

.. tip::
    | The :kbd:`/` key also works for bringing up the Search Bar.
    | Press :kbd:`F3` or :kbd:`Shift F3` to find the next or previous occurrence of the search term.
    | Press :kbd:`Esc` to close the Search Bar.

.. note::
    Search is limited to the commits loaded in memory.
    To find an old commit in a long-lived repository, you may want to review
    |cogwheel| :menuselection:`Settings --> Commit History --> Load up to # commits`.

.. _explore-commit:

Exploring the changes in a commit
---------------------------------

Once you've selected a commit in the Commit History, the lower half of the main window is dedicated to exploring the contents of the commit.

.. _figure-commit-explorer:
.. figure:: /assets/screens/commitexplorer.png

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", () => addFigurePins(
            "#figure-commit-explorer",
            {x:50, y:04, title:'Header'},
            {x:13, y:58, title:'File List'},
            {x:76, y:58, title:'Diff View'},
        ));
    </script>

1. | **Header:** The first line in the commit message.
   | Click :guilabel:`Info` to view detailed metadata about the commit.
   | Click the :gficon:`maximize` maximize button to expand the Commit Explorer.

2. | **File List:** All files modified by this commit in relation to its parents.
   | |lmb| Left-click on a file and the Diff View will show what's changed in it.
   | |rmb| Right-click on a file to :ref:`open a context menu <history-files-cm>` with advanced operations.

3. | **Diff View:** Displays the changes introduced by the commit in the selected file.
   | The Diff View is covered in detail in its own chapter: :doc:`diff`.

.. _back-forward:

Returning to an item you've previously visited
----------------------------------------------

As you navigate your repository, |App| keeps track of where you've been.
Much like a Web browser, you can go "back" and "forward" among the items you've viewed recently.

To return to an item you've previously visited, use the :gficonlabel:`back Back`
and :gficonlabel:`forward Forward` buttons in the Tool Bar, or press
:kbd:`Ctrl ←` and :kbd:`Ctrl →`. You can also use your mouse's back/forward buttons.

.. _chrono-topo:

Advanced: Chronological vs. Topological sorting
-----------------------------------------------

Out of the box, the Commit History displays commits in **chronological** order.
You can switch to **topological** sorting in
|cogwheel| :menuselection:`Settings --> Commit History --> Sort commits`.

**Chronological mode** lets you stay on top of the latest activity in the repository.
The most recent commits always show up at the top of the graph.
However, the graph can get messy when multiple branches receive commits in the same time frame.

.. figure:: /assets/screens/graphchrono.png

    Chronological mode. New commits trickle into the graph in the exact order they are being made, but the intertwining of branches can get messy.

**Topological mode** makes the graph easier to read. It attempts to present sequences of commits within a branch in a linear fashion. Since this is not a strictly chronological mode, you may have to do more scrolling to see the latest changes in various branches.

.. figure:: /assets/screens/graphtopo.png

    Topological mode. Commits are neatly grouped according to the branch they belong to, but chronology isn't respected across different branches.

.. _history-cm-reference:

Context menu reference
----------------------

.. _history-cm:

Commit History context menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|rmb| **Right-click** on any commit in the Commit History to reveal a context menu with the following actions:

.. list-table:: Actions in the Commit History context menu
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - New Branch Here
      - Create a new branch that will point to this commit.
        See :ref:`new-branch`.

    * - Tag This Commit
      - Create a tag on this commit.

    * - Check Out
      - Enter "Detached HEAD" mode on this commit, or switch to a branch pointing here (if any).

    * - Reset HEAD Here
      - Make the current HEAD point to the selected commit.

    * - Cherry Pick
      - Apply the changes from this commit to your working directory.
        See :ref:`cherrypick`.

    * - Revert
      - Undo the changes in this commit. Reversal applied to your working directory.

    * - Export As Patch
      - Format the changes in this commit as a "unified diff" patch file.

    * - Copy Commit Hash
      - Copy this commit's full SHA-1 hash to the clipboard.

    * - Get Info
      - Display the commit's full message, signature, and other details.

.. tip:: |lmb2| Double-click on a commit to **check out** that commit.

.. _history-files-cm:

File List context menu (when exploring a commit)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|rmb| **Right-click** on a file while exploring a commit to reveal a context menu with the following actions:

.. list-table:: Actions in the File List context menu (while exploring a commit from the History)
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - Open Diff in New Window
      - Open this diff in a detached window within |App|.
        The window will be closed when you close this repository.

    * - Open Diff In...
      - Open this diff in an external program.
        Set up the external diff tool in |cogwheel| :menuselection:`Settings --> External Tools`.

    * - Export Diff As Patch
      - Save this change as a "unified diff" patch file.

    * - Revert This Change
      - Undo the changes in this file only. Reversal applied to your working copy.

    * - Restore File Revision
      - Overwrite your working copy of this file with a past revision (As Of/Before the commit).
        **Warning: your copy will be overwritten---make sure you've backed up any pending changes!**

    * - Open File In...
      - View this revision of the file in an external program. Set up the external editor in
        |cogwheel| :menuselection:`Settings --> External Tools`.

    * - Save A Copy
      - Save a copy of a past revision of the file to the location of your choice.

    * - Open Folder
      - Reveal your working copy of this file in your system's file manager
        if the file still exists in your working directory
        (if it doesn't, it may have been deleted or moved by an ulterior commit).

    * - Copy Path
      - Copy the absolute path to this file to the clipboard.
