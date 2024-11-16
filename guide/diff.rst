Reading and Editing Diffs
=========================

The Diff View shows the evolution of a file between two revisions.

It also gives you powerful tools to help you prepare commits with more
precision. You can use it to stage or discard pieces of code at finer levels
than the entire file.

.. figure:: /assets/screens/diffview.png

    The Diff View.

.. tip::
    Press :kbd:`Alt 4` to get keyboard focus on the Diff View.

Old and new revisions
---------------------

The Diff View compares an **old revision** of a file to a **new revision** of
the same file.

Depending on where you're diffing the file, the :gfold:`old` and :gfnew:`new`
revisions being compared vary:

.. list-table::
    :header-rows: 1
    :class: table-cancelfont

    * - Diffing a file in:
      - :gfold:`"Old"` revision is:
      - :gfnew:`"New"` revision is:

    * - An **unstaged** change
      - From the index
      - From your working copy

    * - A **staged** change
      - At the HEAD commit
      - From the index

    * - A commit from the history
      - Before the commit
      - At the commit

.. _hunk-101:

What's in a hunk?
-----------------

The Diff View only displays the sections of the file that have been modified. These sections are called **hunks**.

.. figure:: /assets/screens/diffhunk.png

    A sample hunk.

Each *hunk* consists of:

- A **header line** starting with :gfhunk:`@@`, detailing the line numbers
  affected by the hunk. It's shown in blue.

- A couple of **context lines**, which don't change in either revision of the
  file. They're a visual aid to help you situate the hunk in the file. These are
  shown in black and white.

- | In between the context lines, the meat of the hunk---a block of **modified lines**:
  | :gfold:`Red lines` represent deletions. (They're gone from the new revision.)
  | :gfnew:`Green lines` represent additions. (They appeared in the new revision.)

.. note::
    Are you red/green colorblind? Switch to a yellow/blue color scheme in
    |cogwheel| :menuselection:`Settings --> Code Diff --> Colorblind-friendly color scheme`.

.. _diff-hunk-tools:

Manipulating hunks
------------------

The power of the Diff View is that you can stage and unstage individual
:ref:`hunks <hunk-101>` without staging or unstaging the entire file.

|rmb| **Right-click on a hunk** to reveal these actions:

.. list-table::
    :header-rows: 1
    :widths: 2 2 5

    * - Item
      - Available in
      - Description

    * - Stage Hunk
      - Unstaged change
      - Stage just this hunk; leave other changes alone

    * - Discard Hunk
      - Unstaged change
      - Discard just this hunk; leave other changes alone

    * - Unstage Hunk
      - Staged change
      - Unstage just this hunk; leave other changes alone

    * - Revert Hunk
      - Past commits
      - Undo the changes in this hunk (reversal applied to your working copy)

    * - Export Hunk As Patch
      - Anywhere
      - Save a patch file containing only this hunk in "unified diff" format

.. note::
    If you're not seeing hunk-related actions, make sure your text selection is empty.

.. _diff-line-tools:

Manipulating individual lines
-----------------------------

If hunks aren't granular enough for you, you can even manipulate diffs **line-by-line**.

Select a piece of code with your mouse in the Diff View. Notice the blue outline surrounding the actionable lines:

.. figure:: /assets/screens/diffselection.png

    Blue outline around selected lines in the Diff View. (Color may vary on your system.)

|rmb| **Right-click on a line selection** to reveal similar actions as the hunk
context menu, only these will just apply to your picked lines:

.. list-table::
    :header-rows: 1
    :widths: 2 2 5

    * - Item
      - Available in
      - Description

    * - Stage Lines
      - Unstaged change
      - Stage just these lines; leave other changes alone

    * - Discard Lines
      - Unstaged change
      - Discard just these lines; leave other changes alone

    * - Unstage Lines
      - Staged change
      - Unstage just these lines; leave other changes alone

    * - Revert Lines
      - Past commits
      - Undo the changes in these lines (reversal applied to your working copy)

    * - Export Lines As Patch
      - Anywhere
      - Save a patch file containing only these lines (plus a couple context lines) in "unified diff" format

.. tip::
    | With a selection of **unstaged** lines: press :kbd:`Enter` to stage them or :kbd:`Del` to discard them.
    | With a selection of **staged** lines: press :kbd:`Del` to unstage them.

.. _diff-gutter:

The gutter
----------

Attached to the left side of the code, the **gutter** displays line numbers in
the :gfold:`old` and :gfnew:`new` revisions (left and right columns,
respectively).

.. figure:: /assets/screens/diffgutter.png

    The gutter beside a code hunk. This hunk covers old lines #1-9
    (left) and new lines #1-7 (right). Old lines #4-6 were :gfold:`deleted`, and
    new line #4 was :gfnew:`added` in their place.

As you hover over a line in the gutter, notice that your cursor flips over
(:gfinline:`/assets/screens/right_ptr.png`). This indicates that |lmb| left-clicking
there will select the entire corresponding line in the diff.

To select multiple lines, click on the gutter and drag your mouse to expand the
selection. You can also just click on one line, then :kbd:`Shift`-click on
another line to select all the lines in between.

Some special lines can be double-clicked to select blocks of code effortlessly:

- |lmb2| Double-click the dashed line next to a :gfhunk:`hunk header` to select the entire hunk.

- |lmb2| Double-click the line number for a :gfold:`red` or :gfnew:`green` line to select adjacent red/green lines around it.

Once you've selected lines from the gutter, you can |rmb| right-click to access
the usual line selection actions (stage, discard, etc.).