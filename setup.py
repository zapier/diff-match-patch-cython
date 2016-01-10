#!/usr/bin/env python
from setuptools import setup, find_packages
from Cython.Build import cythonize
import os
import sys


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


if sys.version_info >= (3,):
    subdir = 'python3'
else:
    subdir = 'python2'

setup(
    name='diff-match-patch-cython',
    version='20121119',
    description = "The Diff Match and Patch libraries offer robust algorithms to perform the operations required for synchronizing plain text.",
    long_description = read('README.rst') + "\n\n" + read("CHANGES.rst"),
    packages = ['diff_match_patch'],
    package_dir = {'': subdir},
    ext_modules = cythonize(
        os.path.join(subdir, 'diff_match_patch/diff_match_patch.pyx')),
    author='Neil Fraser',
    url='http://code.google.com/p/google-diff-match-patch/',
    test_suite='diff_match_patch.diff_match_patch_test',
    license = "Apache",
    classifiers = [
        "Topic :: Text Processing",
        "Intended Audience :: Developers",
        "Development Status :: 6 - Mature",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        ]
)
