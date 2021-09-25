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
from os import path, getcwd, name as os_name
from shutil import rmtree

from .git_tools import commit_git
from .system_tools import system


def api(pkg=path.basename(getcwd()), venv=None):
    """add api entries to docs"""
    log(INFO, '*** run sphinx apidoc scripts ***')
    if path.exists("doc/sphinx/api"):
        rmtree("doc/sphinx/api")
    system("sphinx-apidoc -o doc/sphinx/api -f -E %s" % pkg, venv=venv)
    # todo: add file under doc/sphinx/api to git
    commit_git('added `doc/sphinx/api`', add='doc/sphinx/api')


def html(venv=None):
    """build html documentation (using sphinx)"""
    cleanup(venv)
    log(INFO, '*** run sphinx html scripts ***')
    system("sphinx-build -M html ./doc/sphinx/ ./doc/sphinx/_build",
           venv=venv)


def latexpdf(venv=None):
    """build pdf documentation (using sphinx and LaTeX)"""
    log(INFO, '*** run sphinx latexpdf scripts ***')
    system("sphinx-build -M latexpdf ./doc/sphinx/ ./doc/sphinx/_build",
           venv=venv)


def doctest(venv=None):
    """run sphinx doctest"""
    log(INFO, '*** run sphinx doctest scripts ***')
    system("sphinx-build -M doctest ./doc/sphinx/ ./doc/sphinx/_build",
           venv=venv)


def show(venv=None):
    """show html documentation"""
    index_file = './doc/sphinx/_build/html/index.html'
    if os_name == 'posix':
        system("open %s" % index_file, venv=venv)
    elif os_name == 'nt':
        system(index_file, venv=venv)
    else:
        log(INFO, 'find docs at %s' % index_file)


def cleanup(venv=None):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    # system("rm -f -r -v ./doc/sphinx/_build/")
    system("sphinx-build -M clean ./doc/sphinx/ ./doc/sphinx/_build",
           venv=venv)
