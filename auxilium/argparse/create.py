# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from argparse import ArgumentParser
from configparser import ConfigParser

from ..tools.system_tools import create_venv


def arg_parser(parser=None, config=ConfigParser()):
    parser = ArgumentParser() if parser is None else parser
    parser.add_argument(
        '--name',
        default=config.get('create', 'author', fallback=None),
        help='project name')
    parser.add_argument(
        '--slogan',
        default=config.get('create', 'slogan', fallback=None),
        help='project slogan')
    parser.add_argument(
        '--author',
        default=config.get('create', 'author', fallback=None),
        help='project author')
    parser.add_argument(
        '--email',
        default=config.get('create', 'email', fallback=None),
        help='project email')
    parser.add_argument(
        '--url',
        default=config.get('create', 'url', fallback=None),
        help='project url')
    parser.add_argument(
        '--venv',
        nargs='?',
        const=config.get('create', 'venv', fallback='.aux/venv/'),
        default=config.get('create', 'venv', fallback='.aux/venv/'),
        help=create_venv.__doc__)
    parser.add_argument(
        '--commit',
        nargs='?',
        const=config.get('create', 'commit', fallback='Initial commit'),
        default=config.get('create', 'commit', fallback='Initial commit'),
        help='commit on successful creation')
    return parser