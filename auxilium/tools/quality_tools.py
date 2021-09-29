# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO, DEBUG
from os import getcwd
from os.path import basename

from auxilium.tools.system_tools import module


def quality(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code"""
    log(INFO, '🔍  evaluate quality of source code')
    log(DEBUG, '    in ' + getcwd() + ' for ' + pkg)
    return quality_flake8(pkg, venv)


def quality_pylint(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with pylint"""
    log(DEBUG, '  run pylint')
    return module('pylint', pkg, level=INFO, venv=venv)


def quality_flake8(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with flake8"""
    log(DEBUG, '  run flake8')
    return module('flake8', pkg, level=INFO, venv=venv)


def quality_pep8(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with pep8/pep257"""
    log(DEBUG, '  run pycodestyle (aka pep8)')
    res = module('pycodestyle', pkg, level=INFO, venv=venv)
    log(DEBUG, '  run pydocstyle (aka pep257)')
    return res or module('pydocstyle', pkg, level=INFO, venv=venv)
