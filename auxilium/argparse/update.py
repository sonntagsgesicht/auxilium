

from argparse import ArgumentParser
from configparser import ConfigParser


from auxilium.tools.git_tools import commit_git
from auxilium.tools.pip_tools import requirements, install, \
    cleanup as cleanup_site_packages
from auxilium.tools.docmaintain_tools import docmaintain


def arg_parser(parser=None, config=ConfigParser()):
    parser = ArgumentParser() if parser is None else parser
    parser.add_argument(
        '--doc-header',
        action='store_const',
        const=not config.getboolean('update', 'doc-header', fallback=True),
        default=config.getboolean('update', 'doc-header', fallback=True),
        help=docmaintain.__doc__)
    parser.add_argument(
        '--commit',
        nargs='?',
        const=config.get('update', 'commit', fallback='commit'),
        default=config.get('update', 'commit', fallback='commit'),
        help=commit_git.__doc__)
    parser.add_argument(
        '--add',
        action='store_const',
        const=not config.get('update', 'add', fallback=False),
        default=config.get('update', 'add', fallback=False),
        help='add (stage) new or changed files to `git` repo')
    parser.add_argument(
        '--requirements',
        action='store_const',
        const=not config.getboolean('update', 'requirements', fallback=True),
        default=config.getboolean('update', 'requirements', fallback=True),
        help=requirements.__doc__)
    parser.add_argument(
        '--install',
        action='store_const',
        const=not config.getboolean('update', 'install', fallback=False),
        default=config.getboolean('update', 'install', fallback=False),
        help=install.__doc__)
    parser.add_argument(
        '--cleanup',
        action='store_const',
        const=not config.getboolean('update', 'cleanup', fallback=False),
        default=config.getboolean('update', 'cleanup', fallback=False),
        help=cleanup_site_packages.__doc__ + ' (ignores other input)')
    return parser
