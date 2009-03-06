# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='harobed.paster_template.advanced_package',
      version=version,
      description="PasteScript template to create advanced setuptools-enabled package with buildout and namespace support",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='KLEIN Stéphane',
      author_email='stephane@harobed.org',
      url='',
      license='',
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
