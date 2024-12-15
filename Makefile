# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# This rule actually depends on singlehtml,
# but the makefile doesn't enforce this so we can save some time in the CI.
bookpdf:
	chromium --headless --disable-gpu \
		--allow-file-access-from-files \
		--virtual-time-budget=10000 \
		--run-all-compositor-stages-before-draw \
		--generate-pdf-document-outline \
		--no-pdf-header-footer \
		--print-to-pdf=_build/book.pdf \
		"file://${PWD}/_build/singlehtml/book.html?paginate=A4"

fullsite: html singlehtml bookpdf
	cp _build/book.pdf _build/html/_static/GitFourchetteUsersGuide.pdf
	cp _build/singlehtml/book.html _build/html/book.html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
