# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.7, copyright Friday, 01 October 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


import datetime
import logging
import os
import pathlib
import sys

from argparse import ArgumentParser
from configparser import ConfigParser

from auxilium.add_arguments import ArgumentDefaultsAndConstsHelpFormatter
from auxilium.tools.const import CONFIG_PATH, VERBOSITY_LEVELS, ICONS
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

    if not config.getboolean('DEFAULT', 'icons', fallback=os.name == 'posix'):
        ICONS.clear()
        ICONS.update({'error': '!!', 'warn': '!'})

    # ===========================
    # === add argument parser ===
    # ===========================

    epilog = """
if (default: True) a given flag turns its value to False. \
default behavior may depend on current path and project.
set default behavior in `~/%s` and `./%s`."
""" % (CONFIG_PATH, CONFIG_PATH)

    description = """
creates and manages boilerplate python development workflow.
 [ create > code > test > build > deploy ]
"""

    parser = ArgumentParser(
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter)

    sub_parser = parser.add_subparsers(dest='command')

    # === create ===

    help = "creates a new project, repo and virtual environment"
    description = help + """ \
with project file structure from templates which has already set-up
 `venv` virtual python environment to run and test projects isolated
 `git` source code repository for tracking source code changes
 `unittest` suite of tests to ensure the project works as intended
  already-to-use documentation structure build for `sphinx`
"""

    sub_parser.add_parser(
        'create',
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

    # === update ===
    description = "keeps project, repo and dependencies up-to-date"
    sub_parser.add_parser(
        'update',
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

    # === test ==
    description = "checks project integrity " \
                  "by testing using `unittest` framework"
    sub_parser.add_parser(
        'test',
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

    # === documentation ==
    description = "builds project documentation using `sphinx`"
    sub_parser.add_parser(
        'doc',
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

    # === deploy ==
    description = "builds project distribution " \
                  "and deploy releases to `pypi.org`"
    sub_parser.add_parser(
        'build',
        epilog=epilog,
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

    # === invoke python ==
    description = "invokes python in virtual environment"
    sub_parser.add_parser(
        'python',
        epilog='Call python interpreter of virtual environment '
               '(Note: only some standard optional arguments are implemented)',
        description=description,
        formatter_class=ArgumentDefaultsAndConstsHelpFormatter,
        help=description)

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

    verbosity, formatter = VERBOSITY_LEVELS[
        min(args.verbosity, len(VERBOSITY_LEVELS) - 1)]
    logging.basicConfig(level=verbosity, format=formatter)
    logging.log(1, args)

    # check virtual environment
    if args.env \
            and not os.path.exists(args.env) \
            and args.command != 'create' \
            and not args.demo:
        msg = ICONS["warn"] + \
              'did not find a virtual environment at %s. ' % args.env
        logging.log(logging.WARN, msg)
        msg = ICONS[""] + \
            'consider creating one with ' \
            '`auxilium create --update` ' \
            'or use `auxilium -e command [options]`'
        logging.log(logging.WARN, msg)
        sys.exit(1)

    # check demo
    if args.demo:
        logging.log(logging.INFO, ICONS["demo"] +
                    'relax, just starting a demo')

        del_tree(args.demo)
        v = '-' + 'v' * args.verbosity if args.verbosity else ''
        z = '-' + 'x' * args.exit_status if args.exit_status else ''
        e = '-e=' + args.env
        cmd = (' %s %s %s create '
               '--name=%s '
               '--slogan="a demo by auxilium" '
               '--author=auxilium '
               '--email="sonntagsgesicht@icould.com" '
               '--url="https://github.com/sonntagsgesicht/auxilium"') % \
              (v, z, e, args.demo)
        sys.exit(module('auxilium', cmd, level=logging.INFO))

    # check command or print help
    method = getattr(methods, str(args.command), None)
    if method is None:
        print('>>> auxilium -h')
        parser.print_help()
        for key, choice in sub_parser.choices.items():
            print('\n>>> auxilium ' + key + ' -h')
            choice.print_help()
        sys.exit()

    # check project path
    path = os.getcwd()
    pkg = os.path.basename(os.getcwd())
    full_path = os.path.join(path, pkg)

    if not os.path.exists(full_path) \
            and args.command not in ('create', 'python'):
        msg = ICONS["warn"] + \
              'no maintainable project found at %s ' % full_path
        logging.log(logging.WARN, msg)
        msg = ICONS[""] + \
            'consider creating one with `auxilium create` ' \
            '(or did you mean `auxilium python`?)'
        logging.log(logging.WARN, msg)
        sys.exit(1)

    kwargs = vars(args)
    kwargs['path'] = kwargs.get('path', path)
    kwargs['pkg'] = kwargs.get('name', pkg)

    if path not in sys.path:
        sys.path.append(path)

    start = datetime.datetime.now()
    code = method(**kwargs) if method else 1
    if code:
        msg = 'non-zero exit status (failure in `%s`)' % args.command
        logging.log(logging.ERROR, ICONS['error'] + msg)
        if args.exit_status > 2:
            raise Failure(msg)
        if args.exit_status == 2:
            sys.exit(1)
        if args.exit_status == 1:
            sys.exit(0)
        if args.exit_status == 0:
            sys.exit(1)
    exec_time = (datetime.datetime.now() - start)
    logging.log(logging.ERROR, ICONS['OK'] + 'finished in %0.3fs' %
                exec_time.total_seconds())
    sys.exit()


if __name__ == '__main__':
    main()
