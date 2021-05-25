#!/usr/bin/env python

import os

from setuptools import setup

setup(
    use_scm_version={
        'write_to': os.path.join('pre_commit_hooks', '_version.py')
    }
)
