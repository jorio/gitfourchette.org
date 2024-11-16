A Tour of the Main Window
=========================

Once you've created or opened a repository in |App|, the main window presents
you with these elements:

.. _figure-mainwindow:
.. figure:: /assets/screens/mainwindow.png

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", () => addFigurePins(
            "#figure-mainwindow",
            {x:50, y:12, title:"Tab Bar"},
            {x:50, y:33, title:"Commit History"},
            {x: 6, y:50, title:"Sidebar"},
            {x:23, y:78, title:"File List"},
            {x:72, y:78, title:"Diff View"},
            {x:50, y:98, title:"Status Bar"}
        ));
    </script>

1. :ref:`Tab Bar <tour-tab-bar>`: Lets you switch between the open repositories in your session.
2. :ref:`Commit History <tour-big-widgets>`: A list of commits in the repository.
3. :ref:`Sidebar <tour-sidebar>`: Lets you jump to various facets of your repository.
4. :ref:`File List <tour-file-list>`: Files modified by a commit; or list of files with uncommitted changes.
5. :ref:`Diff View <tour-big-widgets>`: Shows what's changed in the selected file.
6. Status bar: Tells you if |App| is busy with a long operation, otherwise displays helpful contextual hints.

.. _tour-tab-bar:

Tab Bar
-------

Use the tab bar to switch between multiple repositories.

|App| remembers open tabs when you quit. It will automatically restore your tabs
next time you launch it.

|lmb2| Double-click a tab to open the repo's root directory in your file manager.

.. _tour-sidebar:

Sidebar
-------

.. figure:: /assets/screens/sidebar.png
    :align: right

    The Sidebar.

The sidebar exposes various facets of your repository:

- :gficon:`git-workdir` :ref:`uncommitted changes in your working directory <uc-101>`;
- :gficon:`git-branch` :doc:`local branches <branches>` (including the "HEAD" :gficon:`git-head`);
- :gficon:`git-remote` :doc:`remote servers and remote-tracking branches <remotes>`;
- :gficon:`git-tag` tags;
- :gficon:`git-stash` :ref:`stashes <stash-changes>`;
- :gficon:`git-submodule` submodules.

From the sidebar, you can:

- |lmb| **Left-click** on any item to jump to it.
- |rmb| **Right-click** on any item to reveal contextual actions.

.. xxx {%gfclear%}

.. _tour-file-list:

File List
---------

The File List shows a list of modified files in the working directory or in a past commit.
In the File List, you can:

- |lmb| **Left-click** on a file to show its changes in the Diff View.
- |rmb| **Right-click** on a file to perform actions on it. Those depend on
  whether you're :ref:`exploring a past commit <history-files-cm>`
  or :ref:`preparing a new commit <uc-files-cm>`.
- Hover over a file to reveal a tooltip with more details about it.

Each file is adorned by a little icon describing its status:

.. list-table::
    :header-rows: 0
    :class: table-cancelfont

    * - :gficon:`status_a` Added
      - :gficon:`status_r` Renamed/moved (and possibly modified)
    * - :gficon:`status_d` Deleted
      - :gficon:`status_t` Type changed (e.g. regular file became a symlink)
    * - :gficon:`status_m` Modified
      - :gficon:`status_u` Merge conflict (only in Uncommitted Changes)

.. _tour-big-widgets:

Commit History & Diff View
--------------------------

Those elements warrant dedicated chapters:

- :doc:`history`
- :doc:`diff`

Handy shortcuts
---------------

.. tip::
    | Press :kbd:`Alt 1` to get keyboard focus on the Sidebar.
    | Press :kbd:`Alt 2` to get keyboard focus on the Commit History.
    | Press :kbd:`Alt 3` to get keyboard focus on the File List.
    | Press :kbd:`Alt 4` to get keyboard focus on the Diff View.
    | Press :kbd:`Ctrl [` to select the previous file in the list.
    | Press :kbd:`Ctrl ]` to select the next file in the list.
