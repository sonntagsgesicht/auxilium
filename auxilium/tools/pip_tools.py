# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO, DEBUG
from os import remove, getcwd
from os.path import basename, exists, join

from .system_tools import module, PYTHON

FREEZE_FILE = '.freeze'
TEMP_REMOVE_FILE = '.site_packages_to_remove'
PIP = 'pip'


def upgrade(path=getcwd(), venv=PYTHON):
    """upgrade `pip`"""
    log(DEBUG, '*** upgrade `pip` ***')
    return module(PIP, 'install --upgrade pip', path=path, venv=venv)


def requirements(path=getcwd(), venv=PYTHON):
    """manage requirements (dependencies) in `requirements.txt`
        and `upgrade_requirements.txt`"""
    log(INFO, '*** setup environment requirements ***')

    res = 0
    if not exists(join(path, FREEZE_FILE)):
        res += module(PIP, "freeze > %s" % FREEZE_FILE, path=path, venv=venv)

    if exists(join(path, "requirements.txt")):
        res += module(PIP, "install -r requirements.txt",
                      path=path, venv=venv)

    if exists(join(path, "upgrade_requirements.txt")):
        res += module(PIP, "install --upgrade -r upgrade_requirements.txt",
                      path=path, venv=venv)
    return res


def install(path=getcwd(), venv=PYTHON):
    """install current project via `pip install -e .`"""
    log(INFO, '*** install project via pip install -e ***')
    return module(PIP, "install --upgrade -e .", path=path, venv=venv)


def uninstall(pkg=basename(getcwd()), path=getcwd(), venv=PYTHON):
    """uninstall current project via `pip uninstall`"""
    log(INFO, '*** uninstall project via pip uninstall ***')
    return module(PIP, "uninstall -y %s" % pkg, path=path, venv=venv)


def cleanup(path=getcwd(), venv=PYTHON):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    res = 0
    if exists(join(path, FREEZE_FILE)):
        res += module(PIP, "freeze --exclude-editable > %s" % TEMP_REMOVE_FILE,
                      path=path, venv=venv)
        res += module(PIP, "uninstall -r %s -y" % TEMP_REMOVE_FILE,
                      path=path, venv=venv)
        remove(TEMP_REMOVE_FILE)

        res += module(PIP, "install --upgrade -r %s" % FREEZE_FILE,
                      path=path, venv=venv)
        remove(join(path, FREEZE_FILE))
    return res
