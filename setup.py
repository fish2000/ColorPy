#!/usr/bin/env python
'''
setup.py - Setup script to install the ColorPy package.

To install the ColorPy package:
From the directory in which the ColorPy distribution was unpacked, run:

python setup.py install

You should now be able to say 'import colorpy' in your programs and use the package.

Creating the distribution:

python setup.py sdist --formats=zip
python setup.py sdist --formats=gztar
python setup.py bdist_wininst
'''

from setuptools import setup

if __name__ == "__main__":
    setup()
