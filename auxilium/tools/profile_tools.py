# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO

from .const import PROFILE_PATH
from .system_tools import shell, module, del_tree


def profile(profile_file=PROFILE_PATH, venv=None):
    """profile performance"""
    log(INFO, '⏱️  run test profiling')
    module('cProfile', '-s tottime %s' % profile_file, venv=venv)
    module('cProfile', '-o .cprofile %s' % profile_file, venv=venv)
    module('pstats', '.cprofile stat', venv=venv)
    shell('snakeviz .cprofile', venv=venv)


def cleanup():
    """remove temporary files"""
    log(INFO, '🧹  clean profile')
    # removed profiling data files
    del_tree(".cprofile")
    return 0