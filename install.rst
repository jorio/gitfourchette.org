Install |App|
====================

.. image:: assets/flathub.svg
   :scale: 100%
   :alt: Get GitFourchette on Flathub
   :align: right
   :target: https://flathub.org/apps/org.gitfourchette.gitfourchette

Ready-made builds
-----------------

This is the easiest way to try out |App|.

- **Recommended: Install the Flatpak**

  `Get it on Flathub <https://flathub.org/apps/org.gitfourchette.gitfourchette>`_, or simply run:

  .. code-block:: bash

          flatpak install flathub org.gitfourchette.gitfourchette

          flatpak run org.gitfourchette.gitfourchette

- Or, grab a standalone AppImage `from the releases <https://github.com/jorio/gitfourchette/releases>`_.

  (The AppImage is self-contained; your desktop environment theme will not apply to it.)

..
    - macOS builds are available although macOS isn't the main target: :gfold:`.............à remplir quand c'est lancé`

..
    .. note:: The AppImage is self-contained; your desktop environment theme will not apply to the AppImage version.

Run from source using your system’s Qt libraries
------------------------------------------------

This method gives you the best integration with your desktop environment.

1. With your system’s package manager, install *pygit2* (v1.14.1 or later), *pygments* and *pyqt6*:

.. list-table::
    :header-rows: 0

    * - Ubuntu 24.10+
      - ``apt install python3-pygit2 python3-pygments python3-pyqt6 libqt6svg6``

    * - Fedora 41+
      - ``dnf install python3-pygit2 python3-pygments python3-pyqt6``

    * - Arch Linux
      - ``pacman -S python-pygit2 python-pygments python-pyqt6 qt6-svg``

2.
    .. code-block:: bash

        git clone https://github.com/jorio/gitfourchette

3.
    .. code-block:: bash

        ./gitfourchette/run.sh

.. note::

    We recommend pygit2 v1.16.0 or later. However, |App| will remain compatible with pygit2 v1.14.1, with a reduced feature set, at least until the current release of Ubuntu provides a newer version of pygit2.

    You can substitute PyQt6 with PySide6. |App| is compatible with both.

Install from source with pip
----------------------------

The only prerequisite to install |App| from source with `pip` is Python 3.10 or newer, which already comes standard with most Linux distributions.

These two commands will install |App| and its dependencies:

.. code-block:: bash

    git clone https://github.com/jorio/gitfourchette
    pip install -e gitfourchette[pyqt6]

Then, simply run ``gitfourchette``.

To uninstall:

.. code-block:: bash

    pip uninstall gitfourchette

.. note::

    If you prefer to use PySide6 instead of PyQt6, install |App| with this command instead:

    .. code-block:: bash

            pip install -e gitfourchette[pyside6]

.. note::

    Installing PyQt6 or PySide6 via pip instead of your system’s package manager
    may cause |App| to ignore your desktop environment theme.
