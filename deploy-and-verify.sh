# A simple script to create source distribute and deploy it to
# a virtualenv; also create sample project

ENV=/tmp/mptenv
VERSION=`python setup.py --version`
SDIST=dist/modern-package-template-$VERSION.tar.gz

# make sdist
rm -rf dist
python setup.py sdist

# setup env
rm -rf $ENV
virtualenv --no-site-packages $ENV
pypm -E $ENV install paste pastescript
$ENV/bin/pip install $SDIST

# create sample project layout
cd /tmp
rm -rf /tmp/sample
yes "" | $ENV/bin/paster create -t modern_package sample
tree -a sample
