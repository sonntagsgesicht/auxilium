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
from logging import log, INFO
from os import system, walk, sep, getcwd, linesep, path
from shutil import rmtree
from textwrap import wrap

PYTHON = 'python3'


def set_timestamp(pkg=path.basename(getcwd()), root=getcwd()):
    pkg = __import__(pkg) if isinstance(pkg, str) else pkg

    for subdir, dirs, files in walk(root):
        for file in files:
            if file.endswith('py'):
                file = path.join(subdir, file)

                # read file lines into list
                f = open(file, 'r')
                lines = list(map(str.rstrip, f.readlines()))
                f.close()

                # set library date
                if file == root + sep + pkg.__name__ + sep + '__init__.py':
                    for i, line in enumerate(lines):
                        if line.startswith('__date__ = '):
                            d = date.today().strftime('%A, %d %B %Y')
                            log(INFO,
                                "set %s.__date__ = %s" % (pkg.__name__, d))
                            lines[i] = "__date__ = '" + d + "'"
                            break

                    f = open(file, 'w')
                    f.write(linesep.join(lines))
                    f.write(linesep)  # last empty line
                    f.close()


def replace_headers(pkg=path.basename(getcwd()), root=getcwd(), test=False):
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

    for subdir, dirs, files in walk(root):
        for file in files:
            if file.endswith('py'):
                file = path.join(subdir, file)
                log(INFO, '\n*** process %s ***\n' % file)

                # read file lines into list
                f = open(file, 'r')
                lines = list(map(str.rstrip, f.readlines()))
                f.close()

                # remove old header
                removed = list()
                while lines and (not lines[0] or lines[0].startswith('#')):
                    removed.append(lines.pop(0).strip())

                # keep first line in script files
                if removed[0].startswith('#!/usr/bin/env'):
                    new_header[0] = removed[0]

                # add new header
                new_lines = new_header + lines

                if test:
                    log(INFO, 'remove : ' + '\nremove : '.join(removed[:20]))
                    log(INFO, '-' * 65)
                    log(INFO, 'add    : ' + '\nadd    : '.join(new_lines[:20]))
                else:
                    log(INFO, '\n'.join(new_lines[:20]))
                    f = open(file, 'w')
                    f.write(linesep.join(new_lines))
                    f.write(linesep)  # last empty line
                    f.close()


def docmaintain(pkg=path.basename(getcwd()), root=getcwd()):
    """update timestamps and file header"""
    log(INFO, '*** run docmaintain scripts ***')
    set_timestamp(pkg, root)
    replace_headers(pkg, root)


def build(python=PYTHON):
    """build package distribution"""
    log(INFO, '*** run setuptools scripts ***')
    system(python + " setup.py build")
    system(python + " setup.py sdist bdist_wheel")
    system(python + "-m twine check dist/*")


def deploy(usr, pwd, python=PYTHON):
    """release on pypi.org"""
    log(INFO, '*** deploy release on pypi.org ***')
    # run setuptools build
    system(python + " setup.py sdist bdist_wheel")
    system(python + " -m twine check dist/*")

    # push to PyPi.org
    cmd = python + " -m twine upload -u %s -p %s" % (usr, pwd)
    cmd += " dist/* #--repository-url https://test.pypi.org/legacy/ dist/*"
    system(cmd)


def cleanup():
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    # remove setuptools release files
    # system("rm -f -r -v ./build/")
    # system("rm -f -r -v ./dist/")
    # system("rm -f -r -v *.egg-info")
    # system("rm -f -r -v .eggs")
    rmtree("./build/")
    rmtree("./dist/")
    rmtree("*.egg-info")
    rmtree(".eggs")
