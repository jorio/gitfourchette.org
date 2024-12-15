Cloning or Creating a Repository
================================

First things first---we need a repository to work on!  Of course, |App| can open
any repository you already have on your disk: go to :menuselection:`File -->
Open Repository` or press :kbd:`Ctrl O`.

But beyond opening an existing repo, you can also **clone** a repository from a
remote, or **initialize** a new repository on your machine.

If you're dipping your toes in Git, I recommend **cloning** a repository so
that you see what |App| is like in a "real" repo that already has some history.
Here's a URL you can try to clone: `https://github.com/libgit2/libgit2`

Cloning a repository from a remote host
---------------------------------------

In Git parlance, *cloning* means to download a repository, typically from a remote host.

Go to :menuselection:`File --> Clone Repository` or press :kbd:`Ctrl Shift N`. The "Clone" dialog appears:

.. figure:: /assets/screens/clone.png

    The Clone dialog.

Let's review the fields and options in this dialog:

.. list-table:: Fields and options in the Clone dialog
    :header-rows: 1
    :widths: 25 75

    * - Choice
      - Description

    * - URL
      - |App| automatically fills in the URL from your clipboard if possible.
        You can use the :guilabel:`ssh`/:guilabel:`https` button to convert
        the URL to another protocol.

    * - Clone into
      - Where to save the repository on your machine.
        This must be an empty directory; it will be created if it doesn't exist.
        |App| automatically suggests a path when you enter an URL, but you can
        click :guilabel:`Browse` to set your own empty directory.  You can also
        type in a path manually; the "~" character will expand to your home
        directory.

    * - Recurse into submodules
      - Tick this to clone the submodules recursively, if the repository has any.
        If you're unsure, just keep this ticked---it doesn't hurt even if there
        are no submodules.

    * - Shallow clone
      - Tick this if you don't need the repository's full commit history.
        This may speed up the download and save some disk space, but you won't
        be able to look up old commits.  Shallow cloning only fetches the most
        recent commits on each branch (you can specify how many).

    * - Log in with custom key file
      - By default, |App| automatically looks for a matching key in your
        :guilabel:`~/.ssh` directory if the remote requires authentication.
        Tick this to bypass automatic key detection and specify a key file to
        connect to this remote.

    * - Status
      - This box will display download progress information.

When you're satisfied with your settings, click the :guilabel:`Clone` button and
wait for the download to complete.

.. xxxx tip:: Press :kbd:`Ctrl Shift N` to clone a repository.

.. note::
    :guilabel:`Log in with custom key file` is particularly useful if you have multiple repos
    requiring different credentials---for example, if you juggle between two accounts for personal
    and work projects.

.. note::
    By default, :guilabel:`Clone into` automatically suggests your *Downloads* folder,
    but you can change the default location to something else.
    After filling in a path for :guilabel:`Clone into`, long-click the :guilabel:`Browse` button
    and choose :guilabel:`Set as default clone location`.

Creating a blank repository from scratch
----------------------------------------

Go to :menuselection:`File --> New Repository` or press :kbd:`Ctrl N`. A folder
picker appears.

In the folder picker, create an **empty** folder for your repo. It's important
that the folder be **empty** to start a blank repository from scratch! (|App|
will ask you to confirm if you give it a non-empty folder.)

Click :guilabel:`Create repo here` when you're ready. Welcome to your new
repository! Some operations, such as creating branches, require that you create
an **initial commit** (see :doc:`commit`).

Initializing a repository from existing sources on your machine
---------------------------------------------------------------

Go to :menuselection:`File --> New Repository` or press :kbd:`Ctrl N`. A folder
picker appears.

Navigate to the root folder of your source code, then click :guilabel:`Create
repo here`.  |App| will ask you to confirm to initialize a repository in a
non-empty folder.

The entire contents of your source tree will now appear as **unstaged files** in
:ref:`Uncommitted Changes <uc-101>`.  At this point, you should **stage** all
relevant files and create the **initial commit** (see :doc:`commit`).

.. xxxx note:: If you picked a folder that is already a valid Git repository (it contains a `.git` directory), |App| will simply open it instead.
