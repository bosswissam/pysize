#! /usr/bin/env python
"""Distribution setup module."""

__requires__ = ('setuptools >=36.3.0', )
"""The list of pre-requisite requirements, needed to run this module."""

from setuptools import setup

setup_params = {
    'use_scm_version': True,
    'setup_requires': [
        'setuptools_scm>=1.15',
    ]
}

__name__ == '__main__' and setup(**setup_params)
