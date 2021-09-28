#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO, DEBUG
from os import getcwd
from os.path import basename, join

from .system_tools import system, python as _python, module, del_tree

PROFILE_FILE = "dev.py"
TEST_DIR = "test"


def test(test_dir=TEST_DIR, venv=None):
    """test code by running tests"""
    log(INFO, '*** run test scripts')
    log(INFO, '    in ' + getcwd() + ' from ' + test_dir)
    return test_unittest(test_dir, venv)


def test_unittest(test_dir=TEST_DIR, venv=None):
    """test code by running unittest"""
    log(DEBUG, '*** run unittest scripts')
    return module(
        'unittest', 'discover %s -v -p "*.py"' % test_dir,
        level=INFO, venv=venv)


def test_pytest(test_dir=TEST_DIR, venv=None):
    """test code by running pytest"""
    log(DEBUG, '*** run pytest scripts')
    return module('pytest', test_dir + ' unittests.py',
                  level=INFO, venv=venv)


def doctests(pkg=basename(getcwd()), venv=None):
    """test code in doc string (doctest)"""
    log(INFO, '*** run doctest scripts')
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


def coverage(pkg=basename(getcwd()), test_dir=TEST_DIR, venv=None):
    """check code coverage of tests"""
    log(INFO, '*** run test coverage scripts')
    log(INFO, '    in ' + getcwd() + ' from ' + test_dir + ' for ' + pkg)
    return coverage_coverage(pkg, test_dir, venv)


def coverage_test(test_dir=TEST_DIR, venv=None):
    """check code coverage of tests with native test"""
    log(DEBUG, '*** run test coverage scripts')
    return module('test', '--coverage -D `pwd`/coverage_data %s' % test_dir,
                  level=INFO, venv=venv)


def coverage_pytest(test_dir=TEST_DIR, venv=None):
    """check code coverage of tests with pytest"""
    log(DEBUG, '*** run pytest cov scripts')
    # --cov=[SOURCE]
    # --cov-fail-under = MIN
    return module('pytest', '--cov %s --cov-fail-under=80 ' % test_dir,
                  level=INFO, venv=venv)


def coverage_coverage(
        pkg=basename(getcwd()), test_dir=TEST_DIR, venv=None):
    """check code coverage of tests with coverage"""
    log(DEBUG, '*** run coverage scripts')
    cmd = 'run --include="%s*"' \
          ' --module unittest discover %s -v -p "*.py"' % (pkg, test_dir)
    res = module('coverage', cmd, venv=venv)
    module('coverage', 'report -m', level=INFO, venv=venv)
    return res


def profile(profile_file=PROFILE_FILE, venv=None):
    """profile performance"""
    log(INFO, '*** run test profiling')
    log(INFO, '    in ' + getcwd() + ' with ' + profile_file)
    module('cProfile', '-s tottime %s' % profile_file, venv=venv)
    module('cProfile', '-o .cprofile %s' % profile_file, venv=venv)
    module('pstats', '.cprofile stat', venv=venv)
    system('snakeviz .cprofile', venv=venv)


def quality(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code"""
    log(INFO, '*** evaluate quality of source code')
    log(INFO, '    in ' + getcwd() + ' for ' + pkg)
    return quality_flake8(pkg, venv)


def quality_pylint(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with pylint"""
    log(DEBUG, '*** run pylint')
    return module('pylint', pkg, level=INFO, venv=venv)


def quality_flake8(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with flake8"""
    log(DEBUG, '*** run flake8')
    return module('flake8', pkg, level=INFO, venv=venv)


def quality_pep8(pkg=basename(getcwd()), venv=None):
    """evaluate quality of source code with pep8/pep257"""
    log(DEBUG, '*** run pycodestyle (aka pep8)')
    res = module('pycodestyle', pkg, level=INFO, venv=venv)
    log(INFO, '*** run pydocstyle (aka pep257)')
    return res or module('pydocstyle', pkg, level=INFO, venv=venv)


def security(pkg=basename(getcwd()), venv=None):
    """evaluate security of source code"""
    log(INFO, '*** evaluate security of source code')
    log(INFO, '    in ' + getcwd() + ' for ' + pkg)
    return security_bandit(pkg, venv=venv)


def security_bandit(pkg=basename(getcwd()), venv=None):
    """run `bandit` on source code """
    log(DEBUG, '*** run `bandit` on source code')
    return module('bandit', '-r -q %s' % pkg, level=INFO, venv=venv)


def cleanup(test_dir=TEST_DIR):
    """remove temporary files"""
    log(INFO, '*** clean environment')
    log(INFO, '    in ' + getcwd() + ' at ' + test_dir)

    # removed pytest data files
    del_tree(".pytest_cache")

    # removed coverage data files incl. files in test dir
    files = ".coverage", "coverage.xml", "htmlcov"
    del_tree(*files)
    del_tree(*(join(test_dir, f) for f in files))

    # removed profiling data files
    del_tree(".cprofile")
    return 0
