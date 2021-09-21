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
from os import system, chdir, getcwd, path
from shutil import rmtree

PYTHON = 'python3'
PROFILE_FILE = "dev.py"
TEST_DIR = "test"


def unittests(test_dir=TEST_DIR, python=PYTHON):
    """test code by running unittests"""
    log(INFO, '*** run unittest scripts ***')
    system(python + ' -m unittest discover %s -v -p "*.py"' % test_dir)
    log(INFO, '*** run pytest scripts ***')
    system(python + ' -m pytest %s' % test_dir)


def doctests(pkg=path.basename(getcwd()), python=PYTHON):
    """test code in doc string (doctest)"""
    log(INFO, '*** run doctest scripts ***')
    system(python + ' -m doctest ')


def profile(profile_file=PROFILE_FILE, python=PYTHON):
    """profile performance"""
    log(INFO, '*** run test profiling ***')
    system(python + ' -m cProfile -s tottime %s' % profile_file)
    system(python + ' -m cProfile -o .cprofile %s' % profile_file)
    system(python + ' -m pstats .cprofile stat')
    # todo check if snakeviz exists
    system('snakeviz .cprofile')


def quality(pkg=path.basename(getcwd()), python=PYTHON):
    """evaluate quality of source code"""
    log(INFO, '*** run code analysis scripts ***')

    log(INFO, '*** run pylint ***')
    system(python + '-m pylint --exit-zero %s' % pkg)

    log(INFO, '*** run flake8 ***')
    system(python + '-m flake8 --exit-zero %s' % pkg)

    log(INFO, '*** run pycodestyle (aka pep8) ***')
    system(python + '-m pycodestyle %s' % pkg)


def security(pkg=path.basename(getcwd()), python=PYTHON):
    """evaluate security of source code"""
    log(INFO, '*** run code security scripts ***')
    system(python + '-m bandit -r %s' % pkg)


def coverage(pkg=path.basename(getcwd()), test_dir=TEST_DIR, python=PYTHON):
    """check code coverage of tests"""
    log(INFO, '*** run pytest cov scripts ***')
    system(python + ' -m pytest -v --cov %s' % test_dir)

    log(INFO, '*** run coverage scripts ***')
    cwd = getcwd()
    chdir(test_dir)
    cmd = python + ' -m coverage run' \
                   ' --include="*%s*"' \
                   ' --omit="*test?.py"' \
                   ' --module unittest discover -v -p "*.py"' % pkg
    system(cmd)
    system(python + ' -m coverage xml')
    system(python + ' -m coverage report')
    system(python + ' -m coverage html')
    chdir(cwd)


def cleanup(test_dir=TEST_DIR):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')

    # removed profiling data files
    # system("rm -f -v .cprofile")
    rmtree(".cprofile")

    # removed coverage data files
    # system("rm -f -v .coverage")
    # system("rm -f -v coverage.xml")
    # system("rm -f -r htmlcov")
    rmtree(".coverage")
    rmtree("coverage.xml")
    rmtree("htmlcov")

    # removed coverage data files from test/
    rmtree("%s/.coverage" % test_dir)
    rmtree("%s/coverage.xml" % test_dir)
    rmtree("%s/htmlcov" % test_dir)
