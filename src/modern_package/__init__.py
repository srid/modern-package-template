import os
import shutil

from paste.util.template import paste_script_template_renderer
from paste.script.templates import Template, var


class ModernPackageTemplate(Template):
    _template_dir = 'templates'
    summary = "Package with distribute and buildout support"
    vars = [
        var('version', 'Version (like 0.1)', default='0.1'),
        var('description', 'One-line description of the package'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        ]

    template_renderer = staticmethod(paste_script_template_renderer)

    def pre(self, command, output_dir, vars):
        if vars['package'].find('.') > 0:
            vars['namespace'] = vars['package'].split('.')
        else:
            vars['namespace'] = [ vars['package'] ]

    def post(self, command, output_dir, vars):
        template_dir = self.template_dir()
        current_dir = os.path.join(output_dir, "src")
        for part in vars['namespace'][:-1]:
            current_dir = os.path.join(current_dir, part)
            if not os.path.exists(current_dir):
                os.makedirs(current_dir)

            shutil.copyfile(
                os.path.join(template_dir, '.namespace__init__.py'),
                os.path.join(current_dir, '__init__.py')
            )
        
        part = vars['namespace'][-1]
        current_dir = os.path.join(current_dir, part)
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)

        shutil.copyfile(
            os.path.join(template_dir, '.normal__init__.py'),
            os.path.join(current_dir, '__init__.py')
        )

