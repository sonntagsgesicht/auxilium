# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from datetime import date
from json import load, dump
from logging import log, INFO, DEBUG
from os import walk, sep, getcwd, linesep
from os.path import basename, join, getmtime, exists
from sys import path
from textwrap import wrap

from .system_tools import python as _python, module, PYTHON, del_tree


LAST_M_FILE = '.aux/last.json'


def set_timestamp(pkg=basename(getcwd()), root=getcwd()):
    pkg = __import__(pkg) if isinstance(pkg, str) else pkg

    for subdir, dirs, files in walk(root):
        for file in files:
            if file.endswith('py'):
                file = join(subdir, file)

                # read file lines into list
                f = open(file, 'r')
                lines = list(map(str.rstrip, f.readlines()))
                f.close()

                # set library date
                if file == root + sep + pkg.__name__ + sep + '__init__.py':
                    for i, line in enumerate(lines):
                        if line.startswith('__date__ = '):
                            d = date.today().strftime('%A, %d %B %Y')
                            a = (pkg.__name__, d, file)
                            log(INFO-1, "set %s.__date__ = %s in %s" % a)
                            lines[i] = "__date__ = '" + d + "'"
                            break

                    f = open(file, 'w')
                    f.write(linesep.join(lines))
                    f.write(linesep)  # last empty line
                    f.close()


def replace_headers(pkg=basename(getcwd()), root=getcwd(), test=False):
    pkg = __import__(pkg) if isinstance(pkg, str) else pkg

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

    last_mtimes = dict()
    if exists(LAST_M_FILE):
        last_mtimes = load(open(LAST_M_FILE, 'r'))

    for subdir, dirs, files in walk(root):
        if sep + '.' not in subdir:
            for file in files:
                if file.endswith('py'):
                    file = join(subdir, file)
                    if last_mtimes.get(file, '') == str(getmtime(file)):
                        continue
                    log(INFO-1, 'update file header of %s' % file)

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

                    if test:
                        log(DEBUG, 'remove : ' + '\nremove : '.join(removed[:20]))
                        log(DEBUG, '-' * 65)
                        log(DEBUG, 'add    : ' + '\nadd    : '.join(new_lines[:20]))
                    else:
                        log(DEBUG, '\n'.join(new_lines[:20]))
                        f = open(file, 'w')
                        f.write(linesep.join(new_lines))
                        f.write(linesep)  # last empty line
                        f.close()
                    last_mtimes[file] = str(getmtime(file))

    dump(last_mtimes, open(LAST_M_FILE, 'w'), indent=2)


def docmaintain(pkg=basename(getcwd()), root=getcwd()):
    """update timestamps and file header"""
    log(INFO, '*** run docmaintain scripts ***')
    path.append(root)
    set_timestamp(pkg, root)
    replace_headers(pkg, root + sep + pkg)


def build(python=PYTHON):
    """build package distribution"""
    log(INFO, '*** build package distribution ***')
    _python("setup.py build", venv=python)
    _python("setup.py sdist --formats=zip", venv=python)
    _python("setup.py sdist bdist_wheel", venv=python)
    module("twine", "check dist/*")


def cleanup(pkg=basename(getcwd())):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    # remove setuptools release files
    del_tree("./build/", "./dist/", pkg + ".egg-info", ".eggs")
