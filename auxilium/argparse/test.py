
from argparse import ArgumentParser
from configparser import ConfigParser

from auxilium.tools.test_tools import quality, security, coverage, \
    cleanup as cleanup_test


def arg_parser(parser=None, config=ConfigParser()):
    parser = ArgumentParser() if parser is None else parser
    parser.add_argument(
        'path',
        nargs='?',
        default=config.get('test', 'path', fallback='test/'),
        help='path to directory where test are found')
    parser.add_argument(
        '--commit',
        nargs='?',
        const=config.get('test', 'commit', fallback='commit tested'),
        help='auto commit on successful test run')
    parser.add_argument(
        '--coverage',
        action='store_const',
        const=not config.getboolean('test', 'coverage', fallback=True),
        default=config.getboolean('test', 'coverage', fallback=True),
        help=coverage.__doc__)
    parser.add_argument(
        '--quality',
        action='store_const',
        const=not config.getboolean('test', 'quality', fallback=True),
        default=config.getboolean('test', 'quality', fallback=True),
        help=quality.__doc__)
    parser.add_argument(
        '--security',
        action='store_const',
        const=not config.getboolean('test', 'security', fallback=True),
        default=config.getboolean('test', 'security', fallback=True),
        help=security.__doc__)
    parser.add_argument(
        '--cleanup',
        action='store_const',
        const=not config.getboolean('test', 'cleanup', fallback=False),
        default=config.getboolean('test', 'cleanup', fallback=False),
        help=cleanup_test.__doc__)
    return parser
