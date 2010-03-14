modern-package-template
========================

modern-package-template is PasteScript template to create a Python project
with modern practices used in the Python world. This means, you will be
able to create a project with support for:

  - buildout
  - Distribute (setup.py)
  - basic documentation (README.txt, NEWS.txt)
  

Install
-------

You can install the template using PyPM_ or pip:

::

    $ pypm install modern-package-template
    
    OR
    
    $ pip install modern-package-template
    
.. _PyPM: http://pypm.activestate.com/


Using
-----

Create a new package with ``modern_package`` template:
    
::

    $ paster create -t modern_package helloworld

To create a package with namespace support:

::

    $ paster create -t modern_package my.new.package package=my.new.package
    
    
Credits
-------

Source code is derived from the `advanced_package`_ template - which is also
licensed under GPLv3 - and differs from it in the following ways:

  - use distribute instead of setuptools
  - use buildout by default
  - a complete buildout.cfg that is usable

.. _advanced_package: http://pypi.python.org/pypi/harobed.paster_template.advanced_package/