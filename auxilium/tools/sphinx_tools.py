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
from os import getcwd, name as os_name
from os.path import exists, basename
from shutil import rmtree

from auxilium.tools.git_tools import commit_git
from .system_tools import system

SPHINX_API_PATH = "doc/sphinx/api"
SPHINX_INDEX_FILE = "./doc/sphinx/_build/html/intro.html"
SPHINX_PATH = "./doc/sphinx/"
SPHINX_BUILD_PATH = "./doc/sphinx/_build"
SPHINX_IN_OUT_PATHS = SPHINX_PATH, SPHINX_BUILD_PATH


def api(pkg=basename(getcwd()), venv=None):
    """add api entries to `sphinx` docs"""
    log(INFO, '📌  run sphinx apidoc scripts')
    if exists(SPHINX_API_PATH):
        rmtree(SPHINX_API_PATH)
    res = 0
    cmd = "sphinx-apidoc -o %s -f -E %s" % (SPHINX_API_PATH, pkg)
    res += system(cmd, venv=venv)
    res += commit_git('added `%s`' % SPHINX_API_PATH)
    return res


def html(venv=None):
    """build html documentation (using `sphinx`)"""
    cleanup(venv)
    if not exists(SPHINX_API_PATH):
        api(venv=venv)
    log(INFO, '📋  run sphinx html scripts')
    return system("sphinx-build -M html %s %s" % SPHINX_IN_OUT_PATHS,
                  venv=venv)


def latexpdf(venv=None):
    """build pdf documentation (using `sphinx` and `LaTeX`)"""
    log(INFO, '📖  run sphinx latexpdf scripts')
    return system("sphinx-build -M latexpdf %s %s" % SPHINX_IN_OUT_PATHS,
                  venv=venv)


def doctest(venv=None):
    """run `sphinx` doctest"""
    log(INFO, '📝  run sphinx doctest scripts')
    return system("sphinx-build -M doctest %s %s " % SPHINX_IN_OUT_PATHS,
                  venv=venv)


def show(venv=None):
    """show html documentation"""
    if os_name == 'posix':
        return system("open %s" % SPHINX_INDEX_FILE, venv=venv)
    if os_name == 'nt':
        return system("start %s" % SPHINX_INDEX_FILE, venv=venv)
    log(INFO, '💡  find docs at %s' % SPHINX_INDEX_FILE)
    return 1


def cleanup(venv=None):
    """remove temporary files"""
    log(INFO, '🧹  clean environment')
    return system("sphinx-build -M clean %s %s" % SPHINX_IN_OUT_PATHS,
                  venv=venv)
