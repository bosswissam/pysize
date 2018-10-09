#! /usr/bin/env python
"""Distribution setup module."""

__requires__ = ("setuptools >=36.3.0",)
"""The list of pre-requisite requirements, needed to run this module."""

import io
import os

from setuptools import find_packages, setup

setup_params = {"use_scm_version": True, "setup_requires": ["setuptools_scm>=1.15"]}

__name__ == "__main__" and setup(**setup_params)



NAME = "pysize"
DESCRIPTION = "Use to quickly measure the size of your python objects."
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    packages=find_packages(exclude=("tests",)),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/bosswissam/pysize",
    author="bosswissam",
    author_email="bosswissam@gmail.com",
)
