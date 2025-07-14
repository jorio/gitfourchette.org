Blame & File History
====================

:gfversion:`New in v1.4.0.`

The **Blame Window** lets you retrace the history of a specific file. It gives you access to:

- A filtered commit history with only the relevant commits that made changes to this file;
- A line-by-line breakdown of the last commit that is responsible for each part of the file.

To open the Blame Window, |rmb| right-click on any file in the File List, then select :guilabel:`Blame File`. This is available both in the Working Directory and while exploring commits.

.. tip::

    After selecting a file, you can press :kbd:`Ctrl L` to open the Blame
    Window.

    You can also drag a file from your system's file manager and drop it on
    |App|'s main window. If the file belongs to the current repository, |App|
    will open a Blame Window for you.

Overview of Blame Window controls
---------------------------------

.. raw:: html

    <div style='height: 10px;'></div>

.. _figure-blamewindow:
.. figure:: /assets/screens/blamewindow.png

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", () => addFigurePins(
            "#figure-blamewindow",
            {x:50, y:02, title:'File History Graph'},
            {x:05, y:11, title:'Back/Forward Buttons'},
            {x:14, y:11, title:'Newer/Older Buttons'},
            {x:97, y:11, title:'Reveal Full Commit'},
            {x:10, y:40, title:'Gutter (Heatmap)'},
            {x:52, y:65, title:'Commit Information Tooltip'},
        ));
    </script>

1. **File History Menu:** Displays the relevant commits that contributed to this file. Pull down this menu to examine an older or newer revision of the file (more details below).
2. :gficon:`back` :gficon:`forward` **Back/Forward Buttons:** Use these to return to a revision that you've looked at previously. You can also use your mouse's back/forward buttons.
3. :gficon:`go-newer` :gficon:`go-older` **Newer/Older Buttons:** Use these to navigate to a newer or older revision in the file's history.
4. :gficon:`go-window` **Reveal Full Commit:** Click this to reveal the current commit in the main window.
5. **Blame Gutter:** Line-by-line revision history (more details below).
6. **Commit Information Tooltip:** Hover over the Gutter to bring up a tooltip with detailed information about a revision.

.. tip::

    |lmb| Hold :kbd:`Shift` while clicking the newer/older buttons to jump to the top/bottom revisions in the history.

The file history menu
---------------------

Pull down the File History menu to reveal a list of commits that directly
contributed to the file (including any uncommitted changes). To explore the
contents of the file at another point of its history, select any commit in the
list.

.. figure:: /assets/screens/blamehistory.png

    The File History menu in the Blame Window.

.. note::

    This list only shows commits that share ancestry with the commit from which
    you initiated the blame. Changes to this file in unmerged (i.e. unrelated)
    branches aren't shown.

    The graph shown in the file history menu is a **simplified** representation
    of commit ancestry chains. That is, a link between two commits in the file
    history graph does not always represent a *direct* parent-child link,
    because any commits that don't contribute to the file are omitted.

The blame gutter
----------------

.. figure:: /assets/screens/blamegutter.png
    :align: right

    The Blame Gutter.

Attached to the left side of the code, the Blame Gutter shows which commit is
responsible for each line in the file. In other words, it tells you
"who is to blame" for each piece of text in the file.

The background colors in the Blame Gutter give you an overview of the age of
each line in the file. Think of these colors as a "heatmap" for recentness: the
deeper the shade of orange, the more recent the line.

Any lines that were directly modified by the exact commit that you've selected
in the File History menu are shown in **bold** in the gutter.

.. note::

    In the gutter's color scheme, the "age" of a line is relative to the
    revision you're viewing. A deep orange means that the line is recent
    *relative to* the revision that is currently selected in the file history
    menu.

Hover over any part of the Blame Gutter to reveal a tooltip with more details about the commit that is to blame for the attached text.

|rmb| Right-click on any section of the Blame Gutter for additional actions:

- :guilabel:`Blame File at Commit` -- Explore the contents of the file as of the
  given commit.
- :guilabel:`Show Commit in Repo` -- Select the given commit in the Main Window
  so you can explore this commit in the broader context of the repository.
- :guilabel:`Get Commit Info` -- Shows essentially the same information as the
  Blame Gutter tooltips, in copy/pastable form.
