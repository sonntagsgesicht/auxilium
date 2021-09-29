# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import name as os_name
from os.path import basename, join, normpath
from sys import executable

PYTHON = basename(executable)

DEMO_PATH = "auxilium_demo"
PROFILE_PATH = "dev.py"
TEST_PATH = normpath('test/')

LAST_M_FILE = normpath('.aux/last.json')
CONFIG_PATH = normpath('.aux/config')
VENV_PATH = normpath('.aux/venv/')

if os_name == 'nt':
    VENV_TAIL = join('Script', PYTHON)
    VENV = join(VENV_PATH, VENV_TAIL)
elif os_name == 'posix':
    VENV_TAIL = join('bin', PYTHON)
    VENV = join(VENV_PATH, VENV_TAIL)
else:
    VENV_TAIL = ''
    VENV = PYTHON
