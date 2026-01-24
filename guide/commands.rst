Custom Commands
===============

:gfversion:`New in v1.3.0.`

You can augment |App|'s capabilities with **custom commands** tailored to your
workflow. These let you launch commands in a terminal directly from |App|.

You can even send items that you manipulate in the UI as **arguments** to the
commands. These include the selected commit, file, branch, etc.

To define custom commands, go to |cogwheel| :menuselection:`Settings --> Custom
Commands` and simply enter some commands (one per line). Here is a useful sample
to get you started:

.. code-block:: bash

    # Feel free to copy/paste this sample into Custom Commands.
    git rebase -i $COMMIT   # &Interactive Rebase
    git rebase --continue   # &Continue Rebase
    ? git rebase --abort    # &Abort Rebase
    git diff $COMMIT HEAD   # Diff Commit With &HEAD

After you click OK in the Settings, notice the `Commands` menu that appears in
the main menu bar. You're now ready to invoke your commands from this menu.

.. figure:: /assets/screens/commandsmenu.png

    The Commands menu that appears once you've defined at least one Custom Command.

.. tip:: If you've chosen to hide the menu bar, you can also access your
  commands via a pulldown menu attached to the :gficonlabel:`terminal Terminal`
  button in the toolbar.

.. tip:: To select which terminal program to use, go to |cogwheel| :menuselection:`Settings --> External Tools --> Terminal`.

Argument placeholders
---------------------

You may use the following placeholders in your commands:

.. list-table::
    :header-rows: 1

    * - Token
      - Description

    * - $COMMIT
      - SHA-1 hash of the selected commit in the history

    * - $FILE
      - Path to the selected file (relative)

    * - $FILEABS
      - Path to the selected file (absolute)

    * - $FILEDIR
      - Path to the selected file's parent directory (relative)

    * - $FILEDIRABS
      - Path to the selected file's parent directory (absolute)

    * - $HEAD
      - SHA-1 hash of the HEAD commit

    * - $HEADBRANCH
      - Ref name of the HEAD branch

    * - $HEADUPSTREAM
      - Ref name of the HEAD branch's upstream

    * - $REF
      - Name of the selected ref in the sidebar (local branches, remote branches, tags)

    * - $REMOTE
      - Name of the selected remote in the sidebar

    * - $WORKDIR
      - Path to the repository's working directory (absolute)

Titles and separators
---------------------

The :code:`#` character starts a **comment** until the end of the line.

If you add a comment after a command (on the same line), then the comment will
serve as the **title** of the command in the menu.

To create a **separator** in the menu, insert a comment line of dashes
(:code:`#---`) in between two commands.

.. code-block:: bash

    echo 'hello world 1'

    # The command above had no custom title.
    # Let's define a custom title for the next one.

    echo 'hello world 2'  # Say Hello (this is a custom title)

    # Let's add a separator in the menu.
    # -----------------

    echo 'hello world 3'

.. figure:: /assets/screens/commandstitlesep.png

    The example above rendered in the Commands menu (separator and custom title).

Keyboard shortcuts
------------------

.. figure:: /assets/screens/commandsaccelerator.png
    :align: right

    A command titled :code:`&Rebase`.

When you set a custom title for a command, you can define an **accelerator key**
for this command by inserting :code:`&` before some letter in the command title.

For example, titling a command :code:`&Rebase` would assign accelerator key :kbd:`R` to the command.

You can trigger accelerator keys in one of two ways:

- Press :kbd:`Ctrl K`, then your command's accelerator key (e.g. :kbd:`Ctrl K` then :kbd:`R`).

  .. note:: Let go of :kbd:`Ctrl K` before pressing the accelerator key.

- Or, pull down the :menuselection:`Commands` menu with :kbd:`Alt C`, then press your accelerator key (e.g. :kbd:`Alt C` then :kbd:`R`).

Confirmation prompt
-------------------

By default, when you trigger any custom command, |App| will give you a chance to
review the prepared command before it's sent to the terminal (with the proper
substitutions).

You can turn off this behavior by unticking the checkbox at |cogwheel|
:menuselection:`Settings --> Custom Commands --> Ask for confirmation before
running any command`.

If you've turned off the confirmation dialog for all commands, you can still
force it to appear before specific commands. To do so, prepend the commands of
your choice with the :code:`?` character. We strongly recommend doing this for
commands that may have destructive effects!

For example, :code:`? git rebase --abort` will *always* ask you to confirm,
*even* if you've unticked `Ask for confirmation`.
