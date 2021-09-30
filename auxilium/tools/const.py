# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Thursday, 30 September 2021
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
VENV_PATH = join('.', normpath('.aux/venv/'))

if os_name == 'nt':
    VENV_TAIL = join('Scripts', PYTHON)
    VENV = join(VENV_PATH, VENV_TAIL)
elif os_name == 'posix':
    VENV_TAIL = join('bin', PYTHON)
    VENV = join(VENV_PATH, VENV_TAIL)
else:
    VENV_TAIL = ''
    VENV = PYTHON

VERBOSITY_LEVELS = 20, 0, 10, 20, 30, 40, 50

DEBUG_FORMATTER = '%(levelname)-7.7s  %(message)s'
INFO_FORMATTER = ' %(message)s'
ERROR_FORMATTER = DEBUG_FORMATTER
SUB_FORMATTER_PREFIX = '|'

_ICONS = {
    'warn': '⛔',
    'error': '🚫',
    'demo': '🍹',
    'build': '🏗',
    'clean': '🧹',
    'coverage': '📑',
    'maintenance': '🛠',
    'missing': '🤷',
    'status': '🚦',
    'commit': '📌',
    'tag': '🏷',
    'push': '📦',
    'upgrade': '🏅',
    'setup': '⚙',
    'install': '🗜',
    'uninstall': '💔',
    'profiling': '⏱',
    'deploy': '🛫',
    'python': '🐍',
    'quality': '🔍',
    'security': '🚨',
    'create': '🪚',
    'finish': '🏁',
    'apidoc': '📌',
    'html': '📋',
    'latexpdf': '📖',
    'doctest': '📝',
    'doctest2': '🔏',
    'show': '💡',
    'venv': '👻',
    'test': '⛑',
}


class IconContainer(dict):
    none = ''
    default = '*'
    length = 3, 1

    def __getitem__(self, item):
        if super(IconContainer, self).__contains__(item):
            value = super(IconContainer, self).__getitem__(item)
            if value is None:
                value = ''
        elif not item:
            value = ''
        else:
            value = '*'
        length, pre = self.__class__.length
        value = value.ljust(length if len(value.encode()) < 4 else length-1)
        return ' ' * pre + value


ICONS = IconContainer(_ICONS)
