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
from os import system, path, getcwd, name as os_name
from shutil import rmtree

PYTHON = 'python3'


def api(pkg=path.basename(getcwd())):
    """add api entries to docs"""
    log(INFO, '*** run sphinx apidoc scripts ***')
    if path.exists("doc/sphinx/api"):
        rmtree("doc/sphinx/api")
    system("sphinx-apidoc -o doc/sphinx/api -f -E %s" % pkg)
    # todo: add file under doc/sphinx/api to git


def html():
    """build html documentation (using sphinx)"""
    log(INFO, '*** run sphinx html scripts ***')
    system("sphinx-build -M clean ./doc/sphinx/ ./doc/sphinx/_build")
    system("sphinx-build -M html ./doc/sphinx/ ./doc/sphinx/_build")


def latexpdf():
    """build pdf documentation (using sphinx and LaTeX)"""
    log(INFO, '*** run sphinx latexpdf scripts ***')
    system("sphinx-build -M latexpdf ./doc/sphinx/ ./doc/sphinx/_build")


def doctest():
    """run sphinx doctest"""
    log(INFO, '*** run sphinx doctest scripts ***')
    system("sphinx-build -M doctest ./doc/sphinx/ ./doc/sphinx/_build")


def quality(pkg=path.basename(getcwd()), python=PYTHON):
    """evaluate quality of documentation structure"""
    log(INFO, '*** run pydocstyle (aka pep257) ***')
    system(python + ' -m pydocstyle %s' % pkg)


def show():
    """show html documentation"""
    index_file = './doc/sphinx/_build/html/index.html'
    if os_name == 'posix':
        system("open %s" % index_file)
    elif os_name == 'nt':
        system(index_file)
    else:
        log(INFO, 'find docs at %s' % index_file)


def cleanup():
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    # system("rm -f -r -v ./doc/sphinx/_build/")
    system("sphinx-build -M clean ./doc/sphinx/ ./doc/sphinx/_build")
