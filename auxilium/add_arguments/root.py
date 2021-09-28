#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from argparse import ArgumentParser
from configparser import ConfigParser

from ..tools.const import VENV


def add_arguments(parser=None, config=ConfigParser()):
    parser = ArgumentParser() if parser is None else parser
    parser.add_argument(
        '-v', '--verbosity',
        action='count',
        default=0,
        help='set logging level '
             '(-v=ALL, -vv=DEBUG, -vvv=INFO, -vvvv=WARNING, -vvvvv=ERROR) '
             '(default: INFO)')

    env = config.get('DEFAULT', 'env', fallback=VENV)
    parser.add_argument(
        '-e', '--env',
        metavar='PATH',
        nargs='?',
        const=config.get('DEFAULT', 'python', fallback=None),
        default=config.get('DEFAULT', 'env', fallback=env),
        help='set path to python executable or virtual environment. '
             'to use system interpreter just set empty flag `-e=`')

    parser.add_argument(
        '-z', '--exit-non-zero',
        action='count',
        default=0,
        help='exit with non zero return code of failure '
             '(-z for non zero return code, -zz for raising exceptions)')

    parser.add_argument(
        '-demo',
        action='store_true',
        help='start demo to creating a repo')

    return parser