#!/usr/bin/env python
"""
Initial code from: https://github.com/audreyr/cookiecutter-pypackage/
"""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'None' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')
