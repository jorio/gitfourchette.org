Fetch, Pull & Push: Syncing Branches With Remotes
=================================================

.. _set-upstream:

Setting an upstream branch
--------------------------

:ref:`Fetch <fetch-branch>` and :ref:`Pull <pull-branch>` are operations that
synchronize a local branch with a remote branch.

Before you can Fetch or Pull a local branch, you must bind it to a remote
branch. That remote branch is then said to be the **upstream** for the local
branch.

You can change a local branch's upstream at any time, even after the branch has
been created. To do so, right-click on the local branch in the Sidebar and
select :guilabel:`Upstream Branch`; a submenu appears, revealing all known remote
branches. Pick the desired remote branch to set as the new upstream.

You can also clear the upstream reference with :guilabel:`Stop tracking upstream branch`
under the same submenu; Fetch and Pull will stop working on this branch.

.. note::
    If the remote branch you're looking for is missing from the
    :guilabel:`Upstream Branch` submenu, your remote-tracking branches might be
    out of date. Right-click on the :gficon:`git-remote` remote in the
    Sidebar and select :guilabel:`Fetch All Remote Branches`, then see if the
    expected remote branch comes up.

.. note::
    Unlike Fetch and Pull, :ref:`Push <push-branch>` doesn't require the
    local branch to have an upstream.

.. _fetch-branch:

Fetching new commits on a branch
--------------------------------

The "fetch" operation downloads new commits from the remote server. It updates
remote-tracking branches only; your local branches are left intact. After a
fetch, you can look at the new commits in the Commit History and decide whether
you want to merge them into your local branch.

You can fetch any **local branch** that has an upstream. Right-click on the
local branch in the Sidebar, then pick :guilabel:`Fetch (upstream name)`. (If
Fetch is grayed out, :ref:`select an upstream <set-upstream>` first.)

You can also fetch a **remote-tracking branch** directly: right-click on it the
Sidebar, then pick :guilabel:`Fetch New Commits`.

You can update all remote-tracking branches at once for any given remote:
right-click on the remote in the Sidebar, then pick :guilabel:`Fetch All Remote
Branches`.

.. _pull-branch:

Pulling new commits into your branch
------------------------------------

The "pull" operation :ref:`fetches <fetch-branch>` the latest commits from a
remote branch, then it integrates them into your local branch, via a merge
commit if necessary.

Pulling is only possible on the **currently checked-out branch**, and it must
have an :ref:`upstream <set-upstream>`.

To pull the current branch, click :gficonlabel:`git-fetch Pull` in the
Tool Bar.

Pulling has one of three outcomes:

- **Remote branch has no new commits:** |App| will tell you that your branch
  is already up-to-date.

- **Remote branch has new commits:** |App| will fast-forward your branch to
  the remote branch.

- **Remote branch has diverged from your local branch:** A merge is necessary to
  reconcile your branch with the remote. You will be asked to resolve the merge
  conflicts, and conclude the merge by creating a merge commit. (See :doc:`conflicts`
  for more information.)

In any case, |App| will tell you what needs to be done to complete
the pull, and you'll have a chance to confirm or cancel.

.. tip:: Press :kbd:`Ctrl Shift P` to pull the current branch.

.. _push-branch:

Pushing a branch to a remote
----------------------------

The "push" operation uploads your commits on a branch to the remote repository.

You can push any **local branch**, even if it's not assigned an upstream:

- **From the Sidebar:** Right-click the local branch you'd like to push,
  then select :guilabel:`Push`.

- **From the Tool Bar:** Click :gficonlabel:`git-push Push`
  to push the currently checked-out branch.

The "Push Branch" dialog appears, where you can review the parameters
before proceeding:

.. figure:: /assets/screens/pushbranch.png

    The Push Branch dialog.

.. list-table:: Fields in the Push Branch dialog
    :header-rows: 1
    :widths: 25 75

    * - Item
      - Description

    * - :guilabel:`Local branch`
      - Select which branch to push among all the local branches in your repository. By default, your
        current branch is selected.

    * - :guilabel:`Push to`
      - By default, the local branch's upstream is automatically selected. But you don't *have*
        to push to the upstream: you can select any remote branch to upload to.
        You can even create a whole new branch on the remote.

    * - :guilabel:`Force push`
      - **USE WITH EXTREME CAUTION---May cause data loss!** If your local branch has diverged
        from the remote branch, the remote server will reject the push. :guilabel:`Force push` lets you
        bypass this restriction and overwrite the remote branch with the contents of your local branch.

    * - :guilabel:`Track this remote branch after pushing`
      - Tick this to set the local branch's upstream to the remote branch you selected for
        :guilabel:`Push to`. (Grayed out if the selected remote branch is already the upstream.)

    * - :guilabel:`Status`
      - This box displays network information during the push.

After a successful push, notice that the remote branch now points to the same
commit as your local branch. The Commit History displays the tip of a remote
branch with a blue-green box, which you should now see next to the purple box
for your local branch (e.g.
:gfinline:`/assets/screens/refbox-lb.png` |nbsp| :gfinline:`/assets/screens/refbox-rb.png`).

.. warning::
    **Don't tick "Force Push" unless you really know what you are doing!**
    Force-pushing is generally frowned upon because it rewrites history for
    other users of the remote.  This might mess up your teammates' workflow
    and/or cause data loss!

.. tip:: Press :kbd:`Ctrl P` to push the current branch.
