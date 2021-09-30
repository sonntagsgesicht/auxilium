# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.6, copyright Thursday, 30 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO

from auxilium.tools.const import ICONS
from auxilium.tools.system_tools import module


def deploy(usr, pwd, python=None):
    """release on `pypi.org`"""
    log(INFO, ICONS["deploy"] + 'deploy release on `pypi.org`')
    # check dist
    module('twine', 'check --strict dist/*', venv=python)
    # push to PyPi.org
    return module("twine", "upload -u %s -p %s dist/*" % (usr, pwd),
                  venv=python)
