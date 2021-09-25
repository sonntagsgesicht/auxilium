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
from os import getcwd, sep, walk, makedirs
from os.path import exists, join
from shutil import move
from zipfile import ZipFile


def create_project(name=None, slogan=None, author=None, email=None,
                   path=getcwd()):
    """create a new python project with auxilium"""
    loc = __file__.split(sep)
    loc[-1] = sep.join(('data', 'pkg.zip'))
    loc = sep.join(loc)

    log(INFO, 'Please enter project details.\n')

    name = input('Enter project name  : ') if name is None else name
    slogan = input('Enter project slogan: ') if slogan is None else slogan
    author = input('Enter author name   : ') if author is None else author
    email = input('Enter author email  : ') if email is None else email

    root_path = path + sep + name
    pkg_path = root_path + sep + name

    # setup project infrastructure
    if exists(root_path):
        msg = 'Project dir %s exists. Cannot create new project.' % root_path
        raise FileExistsError(msg)

    # shutil.copytree(loc, root_path)
    with ZipFile(loc, 'r') as zip_ref:
        zip_ref.extractall(root_path)

    makedirs(pkg_path)
    move(root_path + sep + '__init__.py', pkg_path)

    # setup source directory
    def rp(pth):
        f = open(pth, 'r')
        c = f.read()
        f.close()

        c = c.replace('<email>', email)
        c = c.replace('<author>', author)
        c = c.replace('<doc>', slogan)
        c = c.replace('<name>', name)
        c = c.replace('<date>', date.today().strftime('%A, %d %B %Y'))

        f = open(pth, 'w')
        f.write(c)
        f.close()

    rp(pkg_path + sep + '__init__.py')
    rp(root_path + sep + 'setup.py')
    rp(root_path + sep + 'README.rst')
    rp(root_path + sep + 'HOWTO.rst')
    rp(root_path + sep + 'CHANGES.rst')
    rp(root_path + sep + 'doc' + sep + 'sphinx' + sep + 'doc.rst')

    log(INFO, '')
    log(INFO, 'Created project %s with these files:' % name)

    for subdir, dirs, files in walk(name):
        log(INFO, '')
        for file in files:
            log(INFO, '  ' + join(subdir, file))

    log(INFO, '')
    log(INFO, "Consider a first full run via: 'cd %s; auxilium full;'" % name)
    log(INFO, '')
