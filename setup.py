#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='pyjs',
    version='0.1.0',
    description='A Python Implementation of Javascript style object',
    author='Josh Hernandez',
    author_email='I.Am.Mr.Josh.Hernandez@gmail.com',
    url='https://github.com/josh-hernandez-exe/py-js',
    packages=[
        'pyjs',
    ],
    package_dir={'pyjs': 'pyjs'},
    include_package_data=True,
    install_requires=[
        'six',
    ],
    license="MIT",
    zip_safe=False,
    keywords='pyjs',
    classifiers=[
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)
