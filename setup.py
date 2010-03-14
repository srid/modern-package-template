# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '1.0b1'

setup(name='modern-package-template',
      version=version,
      description="PasteScript template to create a Python project with distribute and buildout support",
      long_description=README + '\n\n' + NEWS,
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
