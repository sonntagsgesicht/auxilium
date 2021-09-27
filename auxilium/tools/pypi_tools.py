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

from .system_tools import python as _python, module, PYTHON


def deploy(usr, pwd, python=PYTHON):
    """release on `pypi.org`"""
    log(INFO, '*** deploy release on pypi.org ***')
    # run setuptools build
    _python("setup.py sdist bdist_wheel", venv=python)
    module('twine', 'check dist/*', venv=python)

    # push to PyPi.org
    cmd = "upload -u %s -p %s" % (usr, pwd)
    cmd += " dist/* #--repository-url https://test.pypi.org/legacy/ dist/*"
    return module('twine', cmd, venv=python)


