# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO
from os import remove, getcwd
from os.path import basename, exists

from .system_tools import module, PYTHON

FREEZE_FILE = '.freeze'
TEMP_REMOVE_FILE = '.site_packages_to_remove'
PIP = 'pip'


def upgrade(python=PYTHON):
    """upgrade `pip`"""
    log(INFO, '*** upgrade `pip` ***')
    module(PIP, 'install --upgrade pip', venv=python)


def requirements(python=PYTHON):
    """manage requirements (dependencies) in `requirements.txt`
        and `upgrade_requirements.txt`"""
    log(INFO, '*** setup environment requirements ***')
    if not exists(FREEZE_FILE):
        module(PIP, "freeze > %s" % FREEZE_FILE, venv=python)
    if exists("requirements.txt"):
        module(PIP, "install -r requirements.txt", venv=python)
    if exists("upgrade_requirements.txt"):
        module(PIP, "install --upgrade -r upgrade_requirements.txt",
               venv=python)


def install(python=PYTHON):
    """install current project via `pip install -e .`"""
    log(INFO, '*** install project via pip install -e ***')
    module(PIP, "install --upgrade -e .", venv=python)


def uninstall(pkg=basename(getcwd()), python=PYTHON):
    """uninstall current project via `pip uninstall`"""
    log(INFO, '*** uninstall project via pip uninstall ***')
    module(PIP, "uninstall -y %s" % pkg, venv=python)


def cleanup(python=PYTHON):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    if exists(FREEZE_FILE):
        module(PIP, "freeze --exclude-editable > %s" % TEMP_REMOVE_FILE,
               venv=python)
        module(PIP, "uninstall -r %s -y" % TEMP_REMOVE_FILE, venv=python)
        remove(TEMP_REMOVE_FILE)

        module(PIP, "install --upgrade -r %s" % FREEZE_FILE, venv=python)
        remove(FREEZE_FILE)
