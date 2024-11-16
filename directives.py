import os
import os.path

import docutils.nodes

import sphinx
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
from docutils.parsers.rst import directives


class CopyImage(SphinxDirective):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = {}
    final_argument_whitespace = False

    def run(self):
        src = directives.path(self.arguments[0])
        src = os.path.join(self.env.app.builder.srcdir, src.removeprefix("/"))
        dst = os.path.join(self.env.app.builder.outdir, '_images', os.path.basename(src))
        print("Copy", src, dst)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        sphinx.util.osutil.copyfile(src, dst)
        return []


class GFIconLabel(SphinxRole):
    def run(self):
        iconName, caption = self.text.split(" ", 1)
        iconNode = docutils.nodes.image(
            uri=f"/assets/icons/{iconName}.svg",
            width="16px",
            height="16px",
            alt="",
            classes=['no-scaled-link', 'gficon'],#, 'gficon'],
        )
        textNode = docutils.nodes.inline(text='\u00A0'+caption)
        group = docutils.nodes.inline(classes=['guilabel'])
        group.append(iconNode)
        group.append(textNode)
        return [group], []


class GFIcon(SphinxRole):
    def run(self):
        node = docutils.nodes.image(
            uri=f"/assets/icons/{self.text}.svg",
            width="16px",
            height="16px",
            alt="",
            classes=["no-scaled-link", "gficon"])
        return [node], []


class GFInline(SphinxRole):
    def run(self):
        node = docutils.nodes.image(uri=self.text, height="16px", alt="")
        node['classes'].extend(['no-scaled-link', 'gficon'])
        return [node], []


def setup(app: Sphinx):
    app.add_directive('copyimage', CopyImage)
    app.add_role('gficon', GFIcon())
    app.add_role('gficonlabel', GFIconLabel())
    app.add_role('gfinline', GFInline())
