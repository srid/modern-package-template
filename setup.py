# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.9'

setup(name='modern-package-template',
      version=version,
      description="PasteScript template to create a Python project with distribute and buildout support",
      long_description="""\
Install
=======

Install the template :

::

    $ pypm install modern-package-template


Using
=====

Create a new package with modern-package-template template :

::
    
    $ paster create -t modern_package helloworld
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sridhar Ratnakumar',
      author_email='srid@nearfar.org',
      url='http://bitbucket.org/srid/modern-package-template/',
      license='GNU General Public License v3',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "Paste",
          "PasteScript",
          "Distribute"
      ],
      entry_points="""
      [paste.paster_create_template]
      modern_package = modern_package:ModernPackageTemplate
      """,
      )
