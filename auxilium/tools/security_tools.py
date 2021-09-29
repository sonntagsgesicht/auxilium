# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO
from os import getcwd
from os.path import basename

from auxilium.tools.system_tools import module


def security(pkg=basename(getcwd()), venv=None):
    """evaluate security of source code"""
    log(INFO, '🚨  evaluate security of source code')
    return security_bandit(pkg, venv=venv)


def security_bandit(pkg=basename(getcwd()), venv=None):
    """run `bandit` on source code """
    return module('bandit', '-r -q %s' % pkg, level=INFO, venv=venv)
