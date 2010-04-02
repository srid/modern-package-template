modern-package-template
=======================

modern-package-template is a `PasteScript template`_ to create an initial layout
for your Python projects using modern tools and practices followed in the Python
community. Thus, your projects will have the following characteristics:

1. Use Distribute_ instead of setuptools as the BDFL himself supports_ it.
2. Buildout_ support, though you are not required to make use of it.
3. ``README.txt`` and ``NEWS.txt`` automatically included in your package
   metadata as ``long_description``, thus making them appear in the PyPI_ page
   for your project.
4. Automatic script (or .exe) creation using Distribute

Here is `a sample project`_ created using modern-package-template.

See the section titled "Roadmap" below for planned features.

.. _PyPI: http://pypi.python.org/
.. _Buildout: http://www.buildout.org/
.. _supports: http://mail.python.org/pipermail/python-dev/2009-October/092678.html
.. _Distribute: http://packages.python.org/distribute/
.. _`PasteScript template`: http://pythonpaste.org/script/developer.html#templates
.. _`a sample project`: http://bitbucket.org/srid/mpt-sample/src/


Getting started
---------------

First install modern-package-template using PyPM_ or pip_:

::

    $ pypm install modern-package-template
    
    OR
    
    $ pip install modern-package-template
    
.. _PyPM: http://pypm.activestate.com/
.. _pip: http://pip.openplans.org/


To create a Python project called "helloworld", run the following command in
your terminal:
    
::

    $ paster create -t modern_package helloworld

You can also, optionally, create `namespace packages`_:

::

    $ paster create -t modern_package my.new.package package=my.new.package
    
.. _`namespace packages`: http://packages.python.org/distribute/setuptools.html#namespace-packages
    
Once you create the project layout, the very first thing you must do is to
review the contents of ``README.txt`` and edit it accordingly.
    
Roadmap
-------

In the next release, I'd like to add support for Sphinx and Sphinx-PyPI-upload
tool, so that developers can upload their sphinx-based documentation to
packages.python.org without having to manually do it themselves.

If you like, please help with working on one of the `new/open issues`_.

.. _`new/open issues`: http://bitbucket.org/srid/modern-package-template/issues/?status=new&status=open
    
Credits
-------

Source code is derived from the `advanced_package`_ template - which is also
licensed under GPLv3.

.. _advanced_package: http://pypi.python.org/pypi/harobed.paster_template.advanced_package/