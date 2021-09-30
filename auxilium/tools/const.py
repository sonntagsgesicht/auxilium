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
SUB_FORMATTER_PREFIX = '| '

ICONS = {
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
    'profiling': '⏱️',
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

    def __getitem__(self, k):
        if super(IconContainer, self).__contains__(k):
            v = super(IconContainer, self).__getitem__(k)
            if v is None:
                return ''
            return ' ' + v.ljust(2)
        return ' * '


if __name__ == '__main__':

    ic = IconContainer(ICONS)
    # ic.setdefault('*')
    for k in tuple(ic.keys()) + ('12', '423'):
        print(ic[k] + ' ' + k, len(ic[k]))
