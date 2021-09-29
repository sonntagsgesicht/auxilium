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
from .system_tools import module, del_tree, join


def coverage(pkg=basename(getcwd()), test_dir=TEST_PATH, venv=None):
    """check code coverage of tests"""
    log(INFO, '📑  run test coverage scripts')
    log(DEBUG, '    in ' + getcwd() + ' from ' + test_dir + ' for ' + pkg)
    return coverage_coverage(pkg, test_dir, venv)


def coverage_test(test_dir=TEST_PATH, venv=None):
    """check code coverage of tests with native test"""
    log(DEBUG, '  run test coverage scripts')
    return module('test', '--coverage -D `pwd`/coverage_data %s' % test_dir,
                  level=INFO, venv=venv)


def coverage_pytest(test_dir=TEST_PATH, venv=None):
    """check code coverage of tests with pytest"""
    log(DEBUG, '  run pytest cov scripts')
    # --cov=[SOURCE]
    # --cov-fail-under = MIN
    return module('pytest', '--cov %s --cov-fail-under=80 ' % test_dir,
                  level=INFO, venv=venv)


def coverage_coverage(
        pkg=basename(getcwd()), test_dir=TEST_PATH, venv=None):
    """check code coverage of tests with coverage"""
    log(DEBUG, '  run coverage scripts')
    cmd = 'run --include="%s*"' \
          ' --module unittest discover %s -v -p "*.py"' % (pkg, test_dir)
    res = module('coverage', cmd, venv=venv)
    module('coverage', 'report -m', level=INFO, venv=venv)
    return res


def cleanup(test_dir=TEST_PATH):
    """remove temporary files"""
    log(INFO, '🧹  clean coverage')
    log(DEBUG, '    in ' + getcwd() + ' at ' + test_dir)

    # removed coverage data files incl. files in test dir
    files = ".coverage", "coverage.xml", "htmlcov"
    del_tree(*files)
    del_tree(*(join(test_dir, f) for f in files))
    return 0
