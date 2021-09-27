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
from os import getcwd, name as os_name
from os.path import exists, basename
from shutil import rmtree

from auxilium.tools.git_tools import commit_git
from .system_tools import system


def api(pkg=basename(getcwd()), venv=None):
    """add api entries to `sphinx` docs"""
    log(INFO, '*** run sphinx apidoc scripts')
    if exists("doc/sphinx/api"):
        rmtree("doc/sphinx/api")
    res = 0
    res += system("sphinx-apidoc -o doc/sphinx/api -f -E %s" % pkg, venv=venv)
    res += commit_git('added `doc/sphinx/api`', add='doc/sphinx/api')
    return res


def html(venv=None):
    """build html documentation (using `sphinx`)"""
    cleanup(venv)
    if not exists("doc/sphinx/api"):
        api(venv=venv)
    log(INFO, '*** run sphinx html scripts')
    return system("sphinx-build -M html ./doc/sphinx/ ./doc/sphinx/_build",
                  venv=venv)


def latexpdf(venv=None):
    """build pdf documentation (using `sphinx` and `LaTeX`)"""
    log(INFO, '*** run sphinx latexpdf scripts')
    return system("sphinx-build -M latexpdf ./doc/sphinx/ ./doc/sphinx/_build",
                  venv=venv)


def doctest(venv=None):
    """run `sphinx` doctest"""
    log(INFO, '*** run sphinx doctest scripts')
    return system("sphinx-build -M doctest ./doc/sphinx/ ./doc/sphinx/_build",
                  venv=venv)


def show(venv=None):
    """show html documentation"""
    index_file = './doc/sphinx/_build/html/intro.html'
    if os_name == 'posix':
        return system("open %s" % index_file, venv=venv)
    if os_name == 'nt':
        return system(index_file, venv=venv)
    log(INFO, 'find docs at %s' % index_file)
    return 1


def cleanup(venv=None):
    """remove temporary files"""
    log(INFO, '*** clean environment')
    # system("rm -f -r -v ./doc/sphinx/_build/")
    return system("sphinx-build -M clean ./doc/sphinx/ ./doc/sphinx/_build",
                  venv=venv)
