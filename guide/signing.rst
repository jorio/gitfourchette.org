Signing Commits
===============

Creating a signed commit
------------------------

:gfversion:`New in v1.5.0:`
The :gficon:`gpg-key` key icon at the bottom of the Commit Dialog indicates whether your commit will be GPG-signed.

:gficon:`gpg-key-green` **A green key** means your commit **will** be signed.

:gficon:`gpg-key-fail` **A gray key** means your commit will **not** be signed.

You can click the key icon to enable or disable signing for the commit you're about to make.

.. figure:: /assets/screens/keybutton.png

    The signing key button in the Commit Dialog.

After making a signed commit, you should see a green seal icon :gficon:`gpg-verify-good-trusted` next to your name in the Commit History.

.. rubric:: What to do if signing isn't available

.. note::

    To be able to sign commits, you must first set up :code:`user.signingKey` in your Git configuration.
    See `Pro Git -- Signing Your Work <https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work>`_ to get started.

- Check that you've set :code:`user.signingKey` in your Git configuration. This is required to specify what key to sign your commits with.
- If you've set up your signing key and you want *all* commits to be signed, check that you've enabled :code:`commit.gpgSign` in your Git configuration.

.. _verify:

Verifying signed commits in the Commit History
----------------------------------------------

:gfversion:`New in v1.5.0:`
To enable automatic verification of signed commits in the Commit History, go to |cogwheel| :menuselection:`Settings --> Commit History` and tick :guilabel:`Verify signed commits on the fly`.

As commits scroll into view, |App| will then call :code:`git verify-commit` automatically to verify their signatures.
The verification status is materialized by a seal icon next to the author's name:

.. list-table::
    :header-rows: 0

    * - :gficon:`gpg-verify-pending` Verification pending
    * - :gficon:`gpg-verify-cantcheck` Verification failed (e.g. missing key)
    * - :gficon:`gpg-verify-good-untrusted` Good signature; Key not fully trusted
    * - :gficon:`gpg-verify-good-trusted` Good signature; Key trusted
    * - :gficon:`gpg-verify-expired` Key or signature expired
    * - :gficon:`gpg-verify-bad` Key revoked or signature invalid
    * - (No seal icon: Commit isn't signed.)

.. rubric:: Troubleshooting failed verifications ("question mark" seal icons)

Your GPG keychain must contain the signer's public key to be able to verify their commits.

Frequently, verification will fail (:gficon:`gpg-verify-cantcheck`) because GPG can't find the signer's public key in your keychain. You can import their public key from a trusted source, then force |App| to verify the commit again (right-click on the commit and select :guilabel:`Verify Signature`).

.. tip::

    You can try :code:`gpg --search-keys` to import a key from your keyserver. For example, the following command lets you import a key owned by GitHub that is commonly used to sign commits made with their web interface:

    .. code-block:: bash

        gpg --search-keys B5690EEEBB952194
