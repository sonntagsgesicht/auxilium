# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO
from os import getcwd
from os.path import basename

from .system_tools import python as _python, module, PYTHON, del_tree


def build(python=PYTHON):
    """build package distribution"""
    log(INFO, '*** build package distribution ***')
    res = 0
    res += _python("setup.py build", venv=python)
    res += _python("setup.py sdist --formats=zip", venv=python)
    res += _python("setup.py sdist bdist_wheel", venv=python)
    res += module("twine", "check dist/*")
    return res


def cleanup(pkg=basename(getcwd())):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    # remove setuptools release files
    del_tree("./build/", "./dist/", pkg + ".egg-info", ".eggs")
    return 0
