Managing Your Branches
======================

.. figure:: /assets/screens/sidebar-branches.png
    :align: right

    Local branches in the Sidebar. |br| "master" is checked out.

All of the :gficon:`git-branch` **local branches** in your repository are listed under
:guilabel:`Local Branches` in the sidebar
(or just :guilabel:`Branches` if the sidebar is narrow).

A little head :gficon:`git-head` is shown next to your current *HEAD* branch,
i.e. the currently checked-out branch.

.. tip:: Press :kbd:`Ctrl H` to jump to the *HEAD*. (Mac: :kbd:`Cmd D`)

.. _new-branch:

Creating a new branch
---------------------

You can start a new branch from several places:

- **From the Commit History:** Right-click on any **commit**, then select :guilabel:`New Branch Here`.
- **From the Sidebar:** Right-click on any **local or remote branch**, then select :guilabel:`New Branch Here`.
- **From the Tool Bar:** Click the :gficonlabel:`git-branch Branch` button to start a branch off the HEAD commit.

After you've triggered one of the actions above, the "New Branch" dialog will let you set up the branch:

.. figure:: /assets/screens/newbranch.png

    The New Branch dialog.

.. list-table:: Fields in the New Branch dialog
    :header-rows: 1
    :widths: 25 75

    * - Item
      - Description

    * - Name
      - You can name your branch however you want, bar some
        `restrictions <https://git-scm.com/docs/git-check-ref-format>`_.
        |App| will let you know if the name you've entered isn't compliant.

    * - Switch to branch after creating
      - Tick this to switch to the new branch after creating it.
        Otherwise, the repository will remain on the current branch.

    * - ...then recurse into submodules
      - Tick this to update the submodules after switching to the new branch.
        (Only available if your repository uses submodules.)

    * - Track upstream branch
      - If a remote branch points to the target commit for the new branch,
        you can make it the upstream for the new branch.
        (You can always :ref:`change the upstream <set-upstream>` later.)

.. tip::
    Press :kbd:`Ctrl B` to create a new branch on the current HEAD commit.

.. _switch-branch:

Switching to another branch
---------------------------

You can switch to another branch from the :ref:`Sidebar <tour-sidebar>`,
or from the :doc:`Commit History <history>`.

- From the Sidebar, |lmb2| double-click any **local branch**. You will be asked to confirm the switch.
  If your repository has any submodules, you will also be asked whether to update them.

- From the Commit History, |lmb2| double-click a **commit** that is the tip of a local branch
  (these commits are adorned with a purple box -- e.g. :gfinline:`/assets/screens/refbox-lb.png`).
  This brings up the "Check out Commit" dialog, which lets you confirm the switch.

After switching to another branch, notice that the :gficon:`git-head` HEAD branch
has changed in the Sidebar, as well as in the Commit History (e.g. :gfinline:`/assets/screens/refbox-lbhead.png`).

.. note::
    You can't switch to a remote branch.
    To achieve something similar, you can create a local branch that tracks the remote branch, then switch to it:
    right-click on the remote branch in the Sidebar then select :guilabel:`New Local Branch Here`.

.. _merge-branch:

Merging another branch into yours
---------------------------------

You can merge any **local or remote branch** into your current branch:

- **From the Sidebar:** Right-click on the branch you'd like to merge from,
  then select :guilabel:`Merge into (current branch)`.

- **From the Commit History:** Right-click on the tip of the branch you'd like to merge from,
  then select :guilabel:`Merge into (current branch)`.

|App| will attempt to **fast-forward** your current branch to the branch you're merging from.
This avoids creating a merge commit.

If fast-forwarding isn't possible, |App| will ask you to resolve the merge conflicts.
hen, conclude the merge by creating a merge commit.
Read :doc:`conflicts` for more details.

.. _branch-folders:

Organizing your branches in folders
-----------------------------------

Your local branches can be organized in :gficon:`git-folder` folders.
Just like paths in a file system, |App| treats the slash character
:guilabel:`/` in a branch name as a "folder separator".

For example, if your repository contains branches :guilabel:`foo/branch1`,
:guilabel:`foo/branch2` and :guilabel:`foo/branch3`, then |App| will group
all three of these under the folder :gficonlabel:`git-folder foo`.

.. note::
    Folders are automatically inferred from the names of your branches; you can't "create" folders per se.
    To conjure up a new folder, rename one of your branches, and insert a slash `/` in its name:
    e.g. rename `mybranch` to `newfolder/mybranch`.

    Folders can be nested. The sidebar will combine chains of nested folders when possible.

|rmb| **Right-click** on a folder to open a context menu
that will let you act on all branches within it. You can:

.. list-table:: Actions in the Branch Folder context menu (from the Sidebar)
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - Rename Folder
      - Rename the part preceding "/" for all branches in the folder.

    * - Delete Folder
      - Delete all local branches in the folder.

    * - Hide Folder
      - Hide all branches in the folder from the commit history.

.. _sort-branches:

Sorting branches in the Sidebar
-------------------------------

To select the sorting mode for your local branches in the Sidebar, right-click
on :guilabel:`Local Branches` and pick an option under :guilabel:`Sort Branches`.

Branches can be sorted:

- by their name, or
- by the date of the latest commit at the tip of each branch.

Note that this will only change the order of the branches in the Sidebar, not in the Commit History.

.. _hide-branches:

Hiding branches in the Commit History
-------------------------------------

You can hide any branch from the Commit History. Move your mouse pointer over
one of the branches in the Sidebar and an eye icon (:gficon:`view-visible`) will
appear. Click it, and the branch will be hidden from the graph, as indicated by
a crossed-out eye icon (:gficon:`view-hidden`) in the sidebar.

.. figure:: /assets/screens/branchhover.png

    Hovering over a branch in the Sidebar.

.. note::
    Even if you hide a branch, it may still be shown in the Commit History if another visible branch points to the same commit.

Sidebar context menu for local branches
---------------------------------------

|rmb| **Right-click** on a local branch in the Sidebar to bring up a context menu with the following actions:

.. list-table:: Actions in the Local Branch context menu (from the Sidebar)
    :header-rows: 1
    :widths: 25 75

    * - Actions
      - Description

    * - Switch to (branch)
      - Switch to the branch (also known as "checking out" the branch).

    * - Merge Into (current branch)
      - Merge the branch into your current branch.
        See also: :doc:`conflicts`.

    * - Fetch (upstream)
      - Download new commits from the :ref:`upstream branch <set-upstream>`,
        but don't bring them into the local branch.
        (You can look at the new commits in the Commit History and decide to merge later on.)
        See :ref:`fetch-branch`.

    * - Pull From (upstream)
      - Download new commits from the :ref:`upstream <set-upstream>`,
        then bring them into the local branch, via a merge commit if necessary.
        See :ref:`pull-branch`.

    * - Fast-forward to (upstream)
      - Move the tip of the branch to the tip of the upstream branch
        (only if that's possible without merging).

    * - Push to (upstream)
      - Publish your new commits to the upstream branch (on the remote).
        See :ref:`push-branch`.

    * - Upstream branch
      - Select which remote branch the local branch should track.
        See :ref:`set-upstream`.

    * - Rename
      - Rename the branch locally (won't affect the upstream branch).

    * - Delete
      - Delete the branch locally (won't affect the upstream branch).

    * - New Branch Here
      - Create a new branch on the same target commit.
        See :ref:`new-branch`.

.. tip::
    | |lmb2| Double-click on a local branch in the Sidebar to **switch** to it.
    | When a local branch has keyboard focus in the Sidebar, hit :kbd:`Enter` to **switch** to it, :kbd:`F2` to **rename** it, or :kbd:`Del` to **delete** it.
