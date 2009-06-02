import os
import shutil

from paste.util.template import paste_script_template_renderer
from paste.script.templates import Template, var

class AdvancedPackageTemplate(Template):
    _template_dir = 'templates'
    summary = "Advanced setuptools-enabled package with buildout and namespace support"
    vars = [
        var('version', 'Version (like 0.1)'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        var('zip_safe', 'True/False: if the package can be distributed as a .zip file', default=False),
        var('buildout', 'True/False: buildout support', default=False),
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
            os.path.join(template_dir, '.__init__.py'),
            os.path.join(current_dir, '__init__.py')
        )

        if (
            (vars['buildout'] == False) or
            (vars['buildout'] == "False") or
            (vars['buildout'] == "") 
        ):
            os.remove(os.path.join(output_dir, "buildout.cfg"))
            os.remove(os.path.join(output_dir, "bootstrap.py"))
