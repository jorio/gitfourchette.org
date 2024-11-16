Making a Commit
===============

This chapter will teach you to create your own commits with |App|.

Crash course: What's in a commit?
---------------------------------

The contents of a Git repository evolve through a series of **commits**.
A commit is a record of the **state of the files** in the repo.

More practically, you can think of a commit as a **small milestone** in your
work on the repository: do some work, then *commit* your work when you're ready
to move on to another task.

In practice, creating a commit entails:

1. Making some modifications to files in the repository (outside |App|);
2. Vetting which file modifications to include in the commit (this is called *staging* the files);
3. Composing a short message that describes the changes since the previous commit.

When you've just finished making the commit, it becomes the **HEAD
commit**---meaning that it's at the tip of the current branch.

Each commit is identified by a unique SHA-1 **hash** of its contents and
metadata (parents, message, signature). Because of this unique hash, commits are
**immutable**: the slightest modification to an existing commit would result in
a different hash, and thereby a different commit.

.. _uc-101:

Jumping to Uncommitted Changes
------------------------------

In |App|, you can prepare commits from the **Uncommitted Changes** view. You can
get there:

- **From the Sidebar:** Click :gficonlabel:`git-workdir Uncommitted Changes` (or just :guilabel:`Changes` if the sidebar is narrow).
- **From the Commit History:** Click :gficonlabel:`git-workdir Uncommitted Changes` at the top of the history.
- **From anywhere:** Press :kbd:`Ctrl U`.

Uncommitted Changes displays any files in your working directory
that have changed since the *HEAD* commit:

.. _figure-uncommitted-changes:
.. figure:: /assets/screens/uncommittedchanges.png

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", () => addFigurePins(
            "#figure-uncommitted-changes",
            {x:18, y:33, title:'Unstaged Files'},
            {x:18, y:75, title:'Staged Files'},
            {x:66, y:56, title:'Diff View'},
        ));
    </script>

1. **Unstaged Changes:** List of files that have changed since the *HEAD* commit,
   but that you haven't *staged* for commit yet.
2. **Staged Changes:** List of changed files that are ready to be committed.
3. **Diff View:** Displays the differences in the selected file between your
   working version and the state of this file at the HEAD commit.

.. note:: The number of changes is shown next to
    :gficonlabel:`git-workdir Uncommitted Changes` in the Sidebar
    if |App| has an up-to-date model of your working directory.

.. _stage-files:

Staging and unstaging files
---------------------------

After you've made some changes to files in the repository (outside of |App|),
the modified files show up in the :guilabel:`Unstaged` box.

To prepare a commit, you must decide which of these files to include in the
commit---this is called **staging** the files. Select some files, then press the
:gficonlabel:`git-stage Stage` button. Notice that the files
you've staged have moved to the :guilabel:`Staged` box.

.. figure:: /assets/screens/stagingarea.png

    The staging area, with some files ready to be committed.

If you change your mind about staging a file, select it in the
:guilabel:`Staged` box, then click :gficonlabel:`git-unstage Unstage`.
The file will move back to the :guilabel:`Unstaged` box.

To get rid of an unwanted modification in the :guilabel:`Unstaged` box, select
the unstaged file and click :gficonlabel:`git-discard Discard`.
(You can :ref:`rescue <rescue-changes>` changes that you've discarded by mistake.)

When you're satisfied with your selection of **staged** files, click the large
:gficonlabel:`git-commit Commit files` button. This brings up the :ref:`Commit
dialog <commit-dialog>` where you can describe your commit and finalize it.

.. tip::
    | Press :kbd:`Alt 3` to get keyboard focus on the file lists.
    | Press :kbd:`Enter` to move the selected files to the other box (unstaged // staged).
    | Press :kbd:`Del` to discard changes to the selected unstaged files.
    | Press :kbd:`Ctrl S` to finalize the commit.
    | Middle-click on a file to stage or unstage it (this behavior must be enabled in |cogwheel| :menuselection:`Settings --> Advanced --> Middle-click file name to stage`).

.. _commit-dialog:

Finalizing the commit (the Commit dialog)
-----------------------------------------

Clicking the :gficonlabel:`git-commit Commit files` button in the main window
brings up the Commit dialog, where you'll be able to type up a commit message
then confirm the commit.

.. figure:: /assets/screens/commitdialog.png

    The Commit dialog.

A commit message consists of:

- A mandatory **summary line**.
  Describe your changes in a few words so other people---including future
  you---can learn what your commit is about at a glance.  Keep it concise:
  proper Git etiquette mandates to keep the summary under 50 characters and to
  avoid going over 72. (The character counter beside this field can help you
  stick to this guideline.)

- An optional **long-form description**.
  Feel free to provide as much context for your changes as necessary in this
  field.

When you're ready, click :guilabel:`Commit`---and you're done!
Notice your new commit in the Commit History: the HEAD branch now points to it, e.g. :gfinline:`/assets/screens/refbox-lbhead.png`.

Your commits are local until you push them
------------------------------------------

So, you've created a commit. But it's just sitting on your machine, for
now---|App| doesn't send it to any remote servers automatically.

Notice that right after creating a commit, your HEAD branch has moved to your
new commit (:gfinline:`/assets/screens/refbox-lbhead.png`) but the remote server
hasn't budged (:gfinline:`/assets/screens/refbox-rb.png`).

This is nice, because it gives you a chance to :ref:`amend <amend>` your commit
before anyone knows you've made a mistake in it.

Once you're satisfied with your work, :ref:`push <push-branch>` your branch to a
remote so the world can see what you've been working on.
