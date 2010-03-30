This file requires editing
==========================

Note to the author: Please add something informative to this README *before*
releasing your software, as `a little documentation goes a long way`_.  Both
README.txt (this file) and NEWS.txt (release notes) will be included in your
package metadata which gets displayed in the PyPI page for your project.

You can take a look at the README.txt of other projects, such as repoze.bfg
(http://bfg.repoze.org/trac/browser/trunk/README.txt) for some ideas.

.. _`a little documentation goes a long way`: http://www.martinaspeli.net/articles/a-little-documentation-goes-a-long-way

Release HOWTO
=============

To make a release, edit "version" in setup.py and run:

  python setup.py egg_info -RDb "" sdist

To upload the generated source distribution to PyPI, run:

  python setup.py egg_info -RDb "" sdist register upload
  
Note that if you ignore the ``egg_info -RDb ""`` part, Distribute will generate
a development release tarball with ``.dev`` marker and SVN revision tag in the
filename. For more details, see:

  http://packages.python.org/distribute/setuptools.html#managing-continuous-releases-using-subversion
  
To disable this behaviour permanently, you can safely delete the file named
"setup.cfg" from your project directory.

