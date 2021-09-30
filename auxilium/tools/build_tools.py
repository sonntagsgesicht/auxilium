# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Thursday, 30 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO
from os import getcwd
from os.path import basename

from auxilium.tools.const import ICONS
from auxilium.tools.system_tools import python as _python, module, del_tree


def build(venv=None):
    """build package distribution"""
    log(INFO, ICONS["build"] + 'build package distribution')
    res = 0
    res += _python("setup.py build", venv=venv)
    res += _python("setup.py sdist --formats=zip", venv=venv)
    # res += _python("setup.py sdist bdist_wheel", venv=venv)
    res += module("twine", "check dist/*")
    return res


def cleanup(pkg=basename(getcwd())):
    """remove temporary files"""
    log(INFO, ICONS["clean"] + 'clean environment')
    # remove setuptools release files
    del_tree("build", "dist")
    return 0
