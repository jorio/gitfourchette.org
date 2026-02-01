Localization
==================

You are welcome to improve an existing translation, or to localize |App| to a new language!

We recommend Weblate to translate the strings.

How to translate via Weblate (recommended)
------------------------------------------

To localize |App|, you can use Weblate, a convenient localization platform. It's quick and easy, no need to set up any development tools!

Head over to `GitFourchette on Weblate <https://hosted.weblate.org/projects/gitfourchette/gitfourchette>`_, pick your language (or create a new one) and translate at your own pace.

.. rubric:: How to preview your Weblate translation in |App|

Once your translation is sufficiently fleshed out, I will ship it with the next release of |App|.

If you don't wait for a merge to preview your work in the UI, you can download an `.mo` file from Weblate for your language
(e.g. `Spanish .mo file <https://hosted.weblate.org/download/gitfourchette/gitfourchette/es/?format=mo>`_).

Rename the file to the two-letter code for your language (e.g. `es.mo`) and drop it into ``gitfourchette/assets/lang``.
If you've done this correctly, |App| should automatically pick up your new language in |cogwheel| :menuselection:`Settings --> General --> Language`.

How to work with .po/.mo files (offline)
----------------------------------------

If you prefer to work offline, this section describes the translation files in ``gitfourchette/assets/lang``.

.. rubric:: Getting to know the 3 kinds of translation files in `gitfourchette/assets/lang`:

- ``gitfourchette.pot`` is a template containing reference U.S. English text.
- ``.po`` files, which you can edit in `POEdit <https://poedit.net>`_.
- ``.mo`` files are compiled binary files that |App| reads from.

.. rubric:: If there's no `.po` file for your language yet:

Create a blank `.po` file from the `gitfourchette.pot` template: Start POEdit and go to :menuselection:`File --> New From POT`, then select ``gitfourchette/assets/lang/gitfourchette.pot``. POEdit will ask you to pick a target language, and you can begin translating.

Save the `.po` file in ``gitfourchette/assets/lang`` and be sure to keep the two-character language name suggested by POEdit.

.. rubric:: To sync your `.po` file with new strings from the source code:

Open your `.po` file in POEdit, then select :menuselection:`Translation --> Update from POT File`.

.. rubric:: To preview your work in |App|:

Generate an `.mo` file beside your `.po` file in ``gitfourchette/assets/lang``. To do this in POEdit, run :menuselection:`File --> Compile to MO`. In GitFourchette, your new language should automatically show up in |cogwheel| :menuselection:`Settings --> General --> Language`.

.. rubric:: Checklist before submitting your translation:

1. In POEdit, run :menuselection:`Translation --> Validate Translations` to make sure you didn't forget any placeholder tokens.
2. If you like, declutter the `.po` file with :menuselection:`Translation --> Purge Deleted Translations`.
3. Commit **just** your `.po` file and open a pull request on GitHub.
4. Don't commit the `.mo` file---I'll regenerate it when I cut a new release of |App|.

.. rubric:: Batch language processing (for maintenance only)

**To sync the `.pot` and `.po` files** with any new strings from the source code **and automatically generate the `.mo` files**, you can run ``./update_resources.py --lang``. Under the hood, this calls `xgettext` and `msgmerge`.

**To declutter the `.po` files,** you can clean up obsolete entries with ``./update-resources.py --clean-po``

Localization guidelines
-----------------------

Git jargon
^^^^^^^^^^

For Git-specific terminology, try to stick to `the translations used by Git itself <https://github.com/git/git/tree/master/po>`_. Note that this isn't a hard rule because I've found that Git translations aren't always consistent.

You can also take a look at the ["Pro Git" book](https://git-scm.com/book) in your language for extra context.

If a jargon term is of utmost importance in Git and it lacks precision in your language, consider keeping it in English, or add the English in parentheses.

For example, I translated "Push branch" to "Publier la branche (push)" in French. I consider "push" to be such an important concept in Git parlance that I want the user to know exactly which operation I'm referring to---but I'm still providing a French word so that somebody with poor English skills will still grasp what "pushing" means.

Length variants
^^^^^^^^^^^^^^^

Occasionally, English strings contain a pipe character ``|``, e.g.: ``Working directory clean|Workdir clean``. For these strings, GitFourchette instructs Qt to use a shorter variant of the string if the full text doesn't fit in its widget.

If the English string contains a pipe character, feel free to define as many variants as you like in your translation---you can add more variants than in English, or you can even just provide a single variant if your language is short enough.
