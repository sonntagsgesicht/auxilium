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

from .const import TEST_PATH
from .system_tools import python as _python, module, del_tree


def test(test_dir=TEST_PATH, venv=None):
    """test code by running tests"""
    log(INFO, '⛑️  run test scripts')
    log(DEBUG, '    in ' + getcwd() + ' from ' + test_dir)
    return test_unittest(test_dir, venv)


def test_unittest(test_dir=TEST_PATH, venv=None):
    """test code by running unittest"""
    log(DEBUG, '  run unittest scripts')
    return module(
        'unittest', 'discover %s -v -p "*.py"' % test_dir,
        level=INFO, venv=venv)


def test_pytest(test_dir=TEST_PATH, venv=None):
    """test code by running pytest"""
    log(DEBUG, '  run pytest scripts')
    return module('pytest', test_dir + ' unittests.py',
                  level=INFO, venv=venv)


def doctests(pkg=basename(getcwd()), venv=None):
    """test code in doc string (doctest)"""
    log(INFO, '🔏  run doctest scripts')
#     cmd = '''
# import doctest, %s as pkg;
# def _doctest_recursively(pkg, *args, **kwargs):
#     import doctest
#     import inspect
#     pkg = __import__(pkg) if isinstance(pkg, str) else pkg
#     if inspect.ismodule(pkg):
#         print(pkg.__name__)
#         return (doctest.testmod(pkg, *args, **kwargs),) + tuple(
#         _doctest_recursively(p) for p in dir(pkg))
# doctest.testmod(pkg, verbose=True)''' % pkg
    cmd = 'import doctest, %s as pkg; doctest.testmod(pkg, verbose=True)' % pkg
    return _python('-c "%s"' % cmd, level=INFO, venv=venv)


def cleanup(test_dir=TEST_PATH):
    """remove temporary files"""
    log(INFO, '🧹  clean test results')
    log(DEBUG, '    in ' + getcwd() + ' at ' + test_dir)

    # removed pytest data files
    del_tree(".pytest_cache")
    return 0
