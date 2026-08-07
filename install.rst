Install |App|
====================

.. image:: assets/flathub.svg
   :scale: 100%
   :alt: Get GitFourchette on Flathub
   :align: right
   :target: https://flathub.org/apps/org.gitfourchette.gitfourchette

Install a pre-built package
---------------------------

- **Recommended: Install the Flatpak**

  `Get it on Flathub <https://flathub.org/apps/org.gitfourchette.gitfourchette>`_, or simply run:

  .. code-block:: bash

          flatpak install flathub org.gitfourchette.gitfourchette

          flatpak run org.gitfourchette.gitfourchette

- Or, grab a standalone AppImage `from the releases <https://github.com/jorio/gitfourchette/releases>`_.

  (The AppImage is self-contained; your desktop environment theme will not apply to it.)

- Unsupported, experimental :ref:`Mac and Windows builds <mac-and-windows>` are also available.

This page also contains instructions to run from source.

Recommended Git version: 2.41 or newer
--------------------------------------

|App| works by calling ``git`` commands for you, so Git must be installed on your system (unless you use the Flatpak version, which comes with Git built in).

|App| integrates best with **Git 2.41 or newer**. If you have an older version of Git, some features may be missing. The oldest supported version is Git 2.34.

.. tip::

    The Flatpak version comes with recent versions of Git and Git-LFS, so you don't have to install them separately. You can still tell the Flatpak version to use your host system's Git install, via |cogwheel| :menuselection:`Settings --> Git Integration`.

How to set up |App| from source
-------------------------------

Using your system's package manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method gives you the best integration with your desktop environment.

1. With your system's package manager, install *pygit2* (v1.14.1 or later), *pygments* and *pyqt6*:

.. list-table::
    :header-rows: 0

    * - Ubuntu 24.10+
      - ``apt install python3-pygit2 python3-pygments python3-pyqt6.qtsvg``

    * - Fedora 41+
      - ``dnf install python3-pygit2 python3-pygments python3-pyqt6``

    * - Arch Linux
      - ``pacman -S python-pygit2 python-pygments python-pyqt6 qt6-svg``

2.
    .. code-block:: bash

        git clone https://github.com/jorio/gitfourchette
        cd gitfourchette
        ./run.sh

.. note::

    We recommend pygit2 v1.14.1 or later.

    You can substitute ``pyqt6`` with ``pyside6`` (version 6.9.0 or later). |App| is compatible with both.

    mfusepy (mount commits with FUSE) is an optional dependency.

Using pip
^^^^^^^^^

The only prerequisite to install |App| from source with ``pip`` is Python 3.10 or newer, which already comes standard with most Linux distributions.

These two commands will install |App| and its dependencies:

.. code-block:: bash

    git clone https://github.com/jorio/gitfourchette
    pip install -e gitfourchette[pyqt6,mfusepy]

Then, simply run: ``gitfourchette``.

To uninstall, run: ``pip uninstall gitfourchette``.

.. note::

    In the ``pip install`` command, you can substitute ``pyqt6`` with ``pyside6``. |App| is compatible with both.

    If you install ``pyqt6`` (or ``pyside6``) using ``pip`` instead of your system's package manager, your desktop environment's native Qt styles ("themes") might not be available in the application.

    mfusepy (mount commits with FUSE) is an optional dependency.
