#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


import logging
import pathlib
import sys
import os

from argparse import ArgumentParser
from configparser import ConfigParser

from auxilium.add_arguments import ArgumentDefaultsAndConstsHelpFormatter
from auxilium.tools.setup_tools import create_project
from auxilium import add_arguments, methods

LEVELS = (logging.INFO, 0, logging.DEBUG,
          logging.INFO, logging.WARNING, logging.ERROR)
Failure = Exception


def main():
    # ==========================
    # === init config parser ===
    # ==========================

    config = ConfigParser(allow_no_value=True)
    config.read(pathlib.Path.home().joinpath('.aux/config'))
    config.read('.aux/config')

    # ===========================
    # === add argument parser ===
    # ===========================

    epilog = \
        "if (default: True) a given flag turns its value to False. " + \
        "default behavior may depend on current path and project. " + \
        "set default behavior in `~/.aux/config` and `./.aux/config`."

    parser = ArgumentParser(
        epilog=epilog, formatter_class=ArgumentDefaultsAndConstsHelpFormatter)

    sub_parser = parser.add_subparsers(dest='command')

    # === create ===
    sub_parser.add_parser(
        'create',
        epilog=epilog,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=create_project.__doc__)

    # === update ===
    sub_parser.add_parser(
        'update',
        epilog=epilog,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help="keep project, repo and dependencies up-to-date")

    # === test ==
    sub_parser.add_parser(
        'test',
        epilog=epilog,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help="check project integrity by testing using `pytest`")

    # === documentation ==
    sub_parser.add_parser(
        'doc',
        epilog=epilog,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help="update project documentation using `sphinx`")

    # === deploy ==
    sub_parser.add_parser(
        'deploy',
        epilog=epilog,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help="manage project deployment")

    # === invoke python ==
    sub_parser.add_parser(
        'python',
        epilog='Call python interpreter of virtual environment '
               '(Note: only some options are implemented)',
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help="invoke (virtual environment) python")

    # ===============================
    # === add arguments to parser ===
    # ===============================

    method = getattr(add_arguments, 'root', None)
    method(parser, config) if method else None

    for k, v in sub_parser.choices.items():
        method = getattr(add_arguments, k, None)
        method(v, config) if method else None

    # ===============================
    # === invoke parsed arguments ===
    # ===============================

    args = parser.parse_args()

    if args.demo:
        cmd = ("rm -f -r auxilium_demo; "
               "auxilium create "
               "--name=auxilium_demo "
               "--slogan='a demo by auxilium'  "
               "--author=auxilium "
               "--email='sonntagsgesicht@icould.com' "
               "--url='https://github.com/sonntagsgesicht/auxilium;'")
        print(cmd)
        sys.exit(os.system(cmd))

    verbosity = LEVELS[min(args.verbosity, len(LEVELS) - 1)]
    log_format = '[%(asctime)s] %(levelname)-12.8s %(message)s'
    if verbosity > logging.DEBUG:
        log_format = '%(message)s'
    logging.basicConfig(level=verbosity, format=log_format)
    logging.log(1, args)

    method = getattr(methods, str(args.command), None)
    if method is None:
        print('>>> auxilium -h')
        parser.print_help()
        for key, choice in sub_parser.choices.items():
            print('\n>>> auxilium ' + key + ' -h')
            choice.print_help()

    path = os.getcwd()
    pkg = os.path.basename(os.getcwd())
    kwargs = vars(args)
    kwargs['path'] = kwargs.get('path', path)
    kwargs['pkg'] = kwargs.get('name', pkg)

    if path not in sys.path:
        sys.path.append(path)

    code = method(**kwargs) if method else 1
    if code:
        if args.exit_non_zero == 2:
            raise Failure('failure in %s' % args.command)
        if args.exit_non_zero == 1:
            sys.exit(1)
    sys.exit()


if __name__ == '__main__':
    main()
