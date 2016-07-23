#!/usr/bin/env python2.7
# coding: utf-8

from setuptools import setup, find_packages

import mdv

setup(
    name='mdv',
    version=mdv.__version__,
    packages=find_packages(),
    author="axiros",
    author_email="",
    description="Terminal Markdown Viewer",
    long_description=open('README.md').read(),
    install_requires=["pyyaml", "pygments", "markdown", "docopt"],
    include_package_data=True,
    url='http://github.com/axiros/terminal_markdown_viewer',
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Topic :: Text Processing :: Markup",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points = {
        'console_scripts': [
            'mdv = mdv:run',
        ],
    },
)