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

from .system_tools import system, PYTHON


def deploy(usr, pwd, python=PYTHON):
    """release on pypi.org"""
    log(INFO, '*** deploy release on pypi.org ***')
    # run setuptools build
    system(python + " setup.py sdist bdist_wheel")
    system(python + " -m twine check dist/*")

    # push to PyPi.org
    cmd = python + " -m twine upload -u %s -p %s" % (usr, pwd)
    cmd += " dist/* #--repository-url https://test.pypi.org/legacy/ dist/*"
    system(cmd)


