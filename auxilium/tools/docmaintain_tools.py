# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from datetime import date
from json import load, dump
from logging import log, INFO, DEBUG
from os import walk, sep, getcwd, linesep, mkdir
from os.path import basename, join, getmtime, exists, split
from sys import path as sys_path
from textwrap import wrap

LAST_M_FILE = '.aux/last.json'


def get_attr(attr, pkg=basename(getcwd()), path=getcwd()):
    default = '<%s>' % attr
    try:
        if path not in sys_path:
            sys_path.append(path)
        pkg = __import__(pkg) if isinstance(pkg, str) else pkg
    except ImportError:
        return default
    return getattr(pkg, '__%s__' % attr, default)


def get_version(pkg=basename(getcwd()), path=getcwd()):
    return get_attr('version', pkg, path)


def get_author(pkg=basename(getcwd()), path=getcwd()):
    return get_attr('author', pkg, path)


def get_url(pkg=basename(getcwd()), path=getcwd()):
    return get_attr('url', pkg, path)


def set_timestamp(pkg=basename(getcwd()), path=getcwd()):
    # pkg = __import__(pkg) if isinstance(pkg, str) else pkg
    pkg = pkg if isinstance(pkg, str) else pkg.__name__
    file = join(path, pkg, '__init__.py')
    # read file lines into list
    f = open(file, 'r')
    lines = list(map(str.rstrip, f.readlines()))
    f.close()
    # make replacement
    for i, line in enumerate(lines):
        if line.startswith('__date__ = '):
            d = date.today().strftime('%A, %d %B %Y')
            a = (pkg, d, file)
            log(DEBUG, "    set %s.__date__ = %s in %s" % a)
            lines[i] = "__date__ = '" + d + "'"
            break
    # write file
    f = open(file, 'w')
    f.write(linesep.join(lines))
    f.write(linesep)  # last empty line
    f.close()


def replace_headers(pkg=basename(getcwd()), last=dict(), path=getcwd()):
    pkg = __import__(pkg) if isinstance(pkg, str) else pkg
    root, _ = split(pkg.__file__)

    new_lines = pkg.__name__,
    new_lines += '-' * len(pkg.__name__),
    new_lines += tuple(wrap(pkg.__doc__))
    new_lines += '',
    new_lines += "Author:   " + pkg.__author__,
    new_lines += "Version:  " + pkg.__version__ + ', copyright ' + pkg.__date__,
    new_lines += "Website:  " + pkg.__url__,
    new_lines += "License:  " + pkg.__license__ + " (see LICENSE file)",
    new_header = ["# -*- coding: utf-8 -*-", '']
    new_header += ['# ' + line for line in new_lines]
    new_header += ['', '']
    new_header = [line.strip() for line in new_header]

    for subdir, dirs, files in walk(root):
        if sep + '.' not in subdir:
            for file in files:
                if file.endswith('.py'):
                    file = join(subdir, file)
                    if last.get(file, '') == str(getmtime(file)):
                        continue
                    log(DEBUG, '    update file header of %s' % file)

                    # read file lines into list
                    f = open(file, 'r')
                    lines = list(map(str.rstrip, f.readlines()))
                    f.close()

                    # remove old header
                    removed = list()
                    while lines and (not lines[0] or lines[0].startswith('#')):
                        removed.append(lines.pop(0).strip())

                    # keep first line in script files
                    if removed and removed[0].startswith('#!/usr/bin/env'):
                        new_header[0] = removed[0]

                    # add new header
                    new_lines = new_header + lines

                    log(DEBUG-1, '\n'.join(new_lines[:20]))
                    f = open(file, 'w')
                    f.write(linesep.join(new_lines))
                    f.write(linesep)  # last empty line
                    f.close()
                    last[file] = str(getmtime(file))
    return last


def docmaintain(pkg=basename(getcwd()), path=getcwd()):
    """update timestamps and file header"""
    log(INFO, '*** run docmaintain scripts')
    log(INFO, '    in ' + path + ' for ' + pkg)
    set_timestamp(pkg, path)

    last_m_file = join(path, LAST_M_FILE)
    if exists(last_m_file):
        last_mtimes = load(open(last_m_file, 'r'))
    else:
        last_mtimes = dict()
    last_mtimes = replace_headers(pkg, last_mtimes, path)
    if not exists(join(path, '.aux')):
        mkdir(join(path, '.aux'))
    dump(last_mtimes, open(last_m_file, 'w'), indent=2)
    return 0
