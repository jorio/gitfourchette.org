Managing Remote Servers and Remote-Tracking Branches
====================================================

.. figure:: /assets/screens/sidebar-remotes.png
    :align: right

    Remotes in the Sidebar

All of the :gficon:`git-remote` **remote servers** added to your repository are listed
under :guilabel:`Remotes` in the sidebar.

In turn, **remote-tracking branches** are listed under their respective remotes.

.. xxx {%gfclear%}

.. _new-remote:

Adding a new remote
-------------------

Right-click on :guilabel:`Remotes` in the sidebar and select :guilabel:`Add Remote`
(or just double-click on :guilabel:`Remotes`) to bring up the "Add Remote" dialog:

.. figure:: /assets/screens/addremote.png

    The Add Remote dialog.

.. list-table:: Fields in the Add Remote dialog
    :header-rows: 1
    :widths: 25 75

    * - Item
      - Description

    * - URL
      - The URL will be used to fetch from, and push to, this remote.
        |App| automatically fills in the URL from your clipboard if possible.
        You can use the :guilabel:`ssh`/:guilabel:`https` button
        to convert the URL to another protocol.

    * - Name
      - You can name the remote however you want, bar some
        `restrictions <https://git-scm.com/docs/git-check-ref-format>`_.
        |App| will let you know if the name you've entered isn't compliant.

    * - Log in with custom key file
      - By default, |App| automatically looks for a matching key in your
        :guilabel:`~/.ssh` directory if the remote requires authentication.
        :guilabel:`Log in with custom key file` lets you bypass automatic key detection
        and specify which key file to use to connect to this remote.

.. note::
    :guilabel:`Log in with custom key file` is particularly useful
    if you have multiple repos requiring different credentials---for example,
    if you juggle between two accounts for personal use and for work.

Sidebar context menu for remotes
--------------------------------

|rmb| Right-click on a **remote** in the sidebar to bring up a context menu with the following actions:

.. list-table:: Actions in the Remote context menu (from the Sidebar)
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - Edit Remote
      - Edit the remote's name, URL, and optional custom key file.
        This is essentially the same dialog as :ref:`Add Remote <new-remote>`.

    * - Fetch All Remote Branches
      - Fetch all remote-tracking branches from this remote.
        After this operation, remote-tracking branches may appear or disappear
        depending on activity on the remote. Won't touch your local branches.

    * - Remove Remote
      - Delete this remote from your local repository.
        Won't have any effect on the server itself.

    * - Visit Web Page
      - Open your web browser to the home page for this repository
        (e.g. on github.com if that's where your repo is hosted).

    * - Copy Remote URL
      - Copies the remote's URL to the clipboard.

.. tip::
    | |lmb2| Double-click on a remote to **edit** it.
    | When a remote has keyboard focus in the sidebar, hit :kbd:`Enter` to **edit** it, or :kbd:`Del` to **remove** it.

Sidebar context menu for remote-tracking branches
-------------------------------------------------

|rmb| Right-click on a **remote-tracking branch** in the sidebar to bring up a context menu with the following actions:

.. list-table:: Actions in the Remote-Tracking Branch context menu (from the Sidebar)
    :header-rows: 1
    :widths: 25 75

    * - Action
      - Description

    * - Start Local Branch From Here
      - Create a new local branch that targets the tip of the remote-tracking branch.

    * - Fetch New Commits
      - Fetch new commits from the remote on this specific remote-tracking branch only.

    * - Merge Into (current branch)
      - Merge the remote-tracking branch into your current local branch.
        This will attempt a fast-forward if possible.
        See also: :doc:`conflicts`.

    * - Rename Branch on Remote
      - Instruct the remote server to rename this branch.
        (This will rename the branch **for all users** of the remote!)

    * - Delete Branch on Remote
      - Instruct the remote server to delete this branch.
        (Make sure this branch **isn't needed by anybody else** that uses this remote!)

    * - Visit Web Page
      - Open your web browser to the page for this branch on the host's web site (e.g. github.com).

.. tip::
    | |lmb2| Double-click on a remote-tracking branch to **start a local branch** from it.
    | When a remote-tracking branch has keyboard focus in the sidebar, hit :kbd:`Enter` to **start a local branch** from it, or :kbd:`Del` to **delete** it from the remote.

Sorting remote-tracking branches in the Sidebar
-----------------------------------------------

Like local branches, remote-tracking branches can be sorted in the sidebar:

- by their name, or
- by the date of the latest commit at the tip of each branch.

To select a sorting mode, right-click on :guilabel:`Remotes` in the sidebar
and pick an option under :guilabel:`Sort Remote Branches By`.