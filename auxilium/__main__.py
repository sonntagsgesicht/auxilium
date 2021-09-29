# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


import logging
import pathlib
import sys
import os

from argparse import ArgumentParser
from configparser import ConfigParser

from auxilium.add_arguments import ArgumentDefaultsAndConstsHelpFormatter
from auxilium.tools.const import CONFIG_PATH, DEMO_PATH, VERBOSITY_LEVELS, \
    DEBUG_FORMATTER, INFO_FORMATTER, ERROR_FORMATTER
from auxilium.tools.setup_tools import create_project
from auxilium.tools.system_tools import module, del_tree
from auxilium import add_arguments, methods

Failure = Exception


def main():
    # ==========================
    # === init config parser ===
    # ==========================

    config = ConfigParser(allow_no_value=True)
    config.read(pathlib.Path.home().joinpath(CONFIG_PATH))
    config.read(CONFIG_PATH)

    # ===========================
    # === add argument parser ===
    # ===========================

    epilog = \
        "if (default: True) a given flag turns its value to False. " + \
        "default behavior may depend on current path and project. " + \
        "set default behavior in `~/%s` and `./%s`." % \
        (CONFIG_PATH, CONFIG_PATH)

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

    verbosity = VERBOSITY_LEVELS[
        min(args.verbosity, len(VERBOSITY_LEVELS) - 1)]

    formatter = DEBUG_FORMATTER
    if verbosity > logging.DEBUG:
        formatter = INFO_FORMATTER
    if verbosity > logging.INFO:
        formatter = ERROR_FORMATTER

    logging.basicConfig(level=verbosity, format=formatter)
    logging.log(1, args)

    # check virtual environment
    if args.env \
            and not os.path.exists(args.env) \
            and args.command != 'create'\
            and not args.demo:
        msg = '⛔   did not find a virtual environment at %s. ' % args.env
        logging.log(logging.WARN, msg)
        msg = '    consider creating one with ' \
              '`auxilium create --update --venv=[PATH]` or ' \
              'use an `-e= ` argument'
        logging.log(logging.WARN, msg)
        sys.exit(1)

    if args.demo:
        logging.log(logging.INFO, '🍹  starting demo - relax')

        del_tree(DEMO_PATH)
        v = '-' + 'v' * args.verbosity if args.verbosity else ''
        z = '-' + 'z' * args.exit_non_zero if args.exit_non_zero else ''
        e = '-e=' + args.env
        cmd = (" %s %s %s create "
               "--name=%s "
               "--slogan='a demo by auxilium'  "
               "--author=auxilium "
               "--email='sonntagsgesicht@icould.com' "
               "--url='https://github.com/sonntagsgesicht/auxilium'") % \
              (v, z, e, DEMO_PATH)
        sys.exit(module('auxilium', cmd, level=logging.INFO))

    method = getattr(methods, str(args.command), None)
    if method is None:
        print('>>> auxilium -h')
        parser.print_help()
        for key, choice in sub_parser.choices.items():
            print('\n>>> auxilium ' + key + ' -h')
            choice.print_help()

    path = os.getcwd()
    pkg = os.path.basename(os.getcwd())
    full_path = os.path.join(path, pkg)

    if not os.path.exists(full_path) \
            and args.command not in ('create', 'python'):
        msg = '⛔   no maintainable project found at %s ' % full_path
        logging.log(logging.WARN, msg)
        msg = '    consider creating one with `auxilium create` ' \
              '(or did you mean `auxilium python`?)'

        logging.log(logging.WARN, msg)
        sys.exit(1)

    kwargs = vars(args)
    kwargs['path'] = kwargs.get('path', path)
    kwargs['pkg'] = kwargs.get('name', pkg)

    # path/project/project

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
