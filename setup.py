# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='harobed.paster_template.advanced_package',
      version=version,
      description="PasteScript template to create advanced setuptools-enabled package with buildout and namespace support",
      long_description="""\

Features supports
=================

* namespace support (handle multiple namespaces levels)
* buildout support

Install
=======

Install the template :

::

    $ sudo easy_install harobed.paster_template.advanced_package


Using
=====

Create a new package with advanced_package template :

::
    
    $ paster create -t advanced_package my.new.package package=my.new.package

You can answer True to buildout question to install buildout files (bootstrap.py and buildout.cfg).
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='KLEIN Stephane',
      author_email='stephane@harobed.org',
      url='http://code.google.com/p/paste-script-advanced-package-template/',
      license='GNU General Public License v3',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages = ['harobed', 'harobed.paster_template'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "Paste",
          "PasteScript",
          "setuptools"
      ],
      entry_points="""
      [paste.paster_create_template]
      advanced_package = harobed.paster_template.advanced_package:AdvancedPackageTemplate
      """,
      )
