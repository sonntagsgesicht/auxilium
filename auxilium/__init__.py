# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.9, copyright Saturday, 02 October 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, basicConfig, getLogger, NullHandler
from os import getcwd, name as os_name
from os.path import basename, split
from pathlib import Path
from sys import exit, executable

from configparser import ConfigParser

from .add_arguments import add_parser
from .methods.root import do
from .tools.const import CONFIG_PATH, VERBOSITY_LEVELS, ICONS


getLogger(__name__).addHandler(NullHandler())


__doc__ = 'Python project for an automated test and deploy toolkit.'
__version__ = '0.1.9'
__dev_status__ = '4 - Beta'
__date__ = 'Saturday, 02 October 2021'
__author__ = 'sonntagsgesicht'
__email__ = __author__ + '@icloud.com'
__url__ = 'https://github.com/' + __author__ + '/' + __name__
__license__ = 'Apache License 2.0'
__dependencies__ = 'pip', 'dulwich', 'flake8', 'bandit', 'coverage', \
                   'sphinx', 'sphinx-rtd-theme', 'sphinx-math-dollar', \
                   'twine', 'karma-sphinx-theme', 'sphinx-nameko-theme'
__dependency_links__ = ()
__data__ = ('data/pkg.zip',)
__scripts__ = ('auxilium=auxilium:main',)


def main():

    # init config and argument parser
    config = ConfigParser(allow_no_value=True)
    config.read(Path.home().joinpath(CONFIG_PATH))
    config.read(CONFIG_PATH)

    # set icons set
    if not config.getboolean('DEFAULT', 'icons', fallback=os_name == 'posix'):
        ICONS.clear()
        ICONS.update({'error': '!!', 'warn': '!'})

    # pars arguments
    parser = add_parser(config)
    args = parser.parse_args()
    kwargs = vars(args)

    # add pkg and path to kwargs
    kwargs['cwd'] = kwargs.get('cwd', getcwd())
    kwargs['path'] = kwargs.get('path', getcwd())
    kwargs['pkg'] = kwargs.get('name', basename(getcwd()))

    # check version
    if args.version:
        print('%s %s from %s (%s)' % (
            __name__, __version__, split(__file__)[0], executable))
        exit()

    # print help in case of no command
    if args.command is None and not any((args.demo, args.version)):
        parser.print_help()
        exit()

    # init logging
    item = min(args.verbosity, len(VERBOSITY_LEVELS) - 1)
    verbosity, formatter = VERBOSITY_LEVELS[item]
    basicConfig(level=verbosity, format=formatter)
    log(1, ICONS['inspect'] + '(parsed) arguments:')
    for item in kwargs.items():
        log(1, ICONS[''] + "  %-12s : %r" % item)

    # call command/method
    do(**kwargs)
