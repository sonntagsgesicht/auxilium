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
import os
from logging import log, INFO
from os import getcwd, path

from .system_tools import system, python as _python, module, PYTHON, del_tree

PROFILE_FILE = "dev.py"
TEST_DIR = "test"


def unittests(test_dir=TEST_DIR, python=PYTHON):
    """test code by running unittests"""
    log(INFO, '*** run unittest scripts ***')
    ut = module('unittest', 'discover %s -v -p "*.py"' % test_dir)
    log(INFO, '*** run pytest scripts ***')
    pt = module('pytest', test_dir, venv=python)
    return ut or pt


def doctests(pkg=path.basename(os.getcwd()), python=PYTHON):
    """test code in doc string (doctest)"""
    log(INFO, '*** run doctest scripts ***')
    # return module('doctest', venv=python)
    # todo search vor doctests recursively
    cmd = '''
import doctest, %s as pkg; 
def _doctest_recursively(pkg, *args, **kwargs):
    import doctest
    import inspect
    pkg = __import__(pkg) if isinstance(pkg, str) else pkg
    if inspect.ismodule(pkg):
        print(pkg.__name__)
        return (doctest.testmod(pkg, *args, **kwargs),) + tuple(
        _doctest_recursively(p) for p in dir(pkg))  
doctest.testmod(pkg, verbose=True)''' % pkg
    cmd = 'import doctest, %s as pkg; doctest.testmod(pkg, verbose=True)' % pkg
    return _python('-c "%s"' % cmd, venv=python)


def profile(profile_file=PROFILE_FILE, python=PYTHON):
    """profile performance"""
    log(INFO, '*** run test profiling ***')
    module('cProfile', '-s tottime %s' % profile_file, venv=python)
    module('cProfile', '-o .cprofile %s' % profile_file, venv=python)
    module('pstats', '.cprofile stat', venv=python)
    # todo check if snakeviz exists
    system('snakeviz .cprofile')


def quality(pkg=path.basename(getcwd()), python=PYTHON):
    """evaluate quality of source code"""
    log(INFO, '*** run code analysis scripts ***')

    log(INFO, '*** run pylint ***')
    module('pylint', pkg, venv=python)

    log(INFO, '*** run flake8 ***')
    module('flake8', pkg, venv=python)

    log(INFO, '*** run pycodestyle (aka pep8) ***')
    module('pycodestyle', pkg, venv=python)

    log(INFO, '*** run pydocstyle (aka pep257) ***')
    module('pydocstyle', pkg)


def security(pkg=path.basename(getcwd()), python=PYTHON):
    """evaluate security of source code"""
    log(INFO, '*** run code security scripts ***')
    return module('bandit', '-r %s' % pkg, venv=python)


def coverage(pkg=path.basename(getcwd()), test_dir=TEST_DIR, python=PYTHON):
    """check code coverage of tests"""

    log(INFO, '*** run test coverage scripts ***')
    module('test', '--coverage -D `pwd`/coverage_data %s' % test_dir,
           venv=python)

    log(INFO, '*** run pytest cov scripts ***')
    module('pytest', '-v --cov %s' % test_dir, venv=python)

    log(INFO, '*** run coverage scripts ***')
    cmd = 'run' \
          ' --include="*%s*"' \
          ' --omit="*test?.py"' \
          ' --module unittest discover -v -p "*.py"' % pkg
    module('coverage', cmd, path=test_dir, venv=python)
    module('coverage', 'xml', path=test_dir, venv=python)
    module('coverage', 'report', path=test_dir, venv=python)
    module('coverage', 'html', path=test_dir, venv=python)


def cleanup(test_dir=TEST_DIR):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')

    # removed pytest data files
    del_tree(".pytest_cache")

    # removed coverage data files incl. files in test dir
    files = ".coverage", "coverage.xml", "htmlcov"
    del_tree(*files)
    del_tree(*(path.join(test_dir, f) for f in files))

    # removed profiling data files
    del_tree(".cprofile")
