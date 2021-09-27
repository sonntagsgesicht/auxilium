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
from logging import log, INFO
from os import getcwd, sep, walk, makedirs
from os.path import exists, join, basename
from shutil import move
from zipfile import ZipFile


def create_project(name=None, slogan=None, author=None, email=None, url=None,
                   path=getcwd()):
    """create a new python project"""
    loc = __file__.split(sep)[:-1]
    loc[-1] = sep.join(('data', 'pkg.zip'))
    loc = sep.join(loc)

    if not any((name, slogan, author, email)):
        log(INFO, '')
        log(INFO, 'Please enter project details.')
        log(INFO, '')

    name = input('Enter project name  : ') if name is None else name
    slogan = input('Enter project slogan: ') if slogan is None else slogan
    slogan += ' (created with auxilium)'
    author = input('Enter author name   : ') if author is None else author
    email = input('Enter project email : ') if email is None else email
    url = input('Enter project url   : ') if url is None else url
    url = url or 'https://github.com/<author>/<name>'

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

        c = c.replace('<url>', url)
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
    rp(root_path + sep + 'doc' + sep + 'sphinx' + sep + 'conf.py')

    log(INFO, '')
    log(INFO, '*** Created project %s with these files:' % name)
    log(INFO, '    in %s' % path)
    for subdir, dirs, files in walk(name):
        log(INFO, '')
        for file in files:
            log(INFO, '      ' + join(subdir, file))
    log(INFO, '')
    return root_path


def create_finish(name=basename(getcwd())):
    log(INFO, '')
    log(INFO, 'Consider a first full run via: ')
    log(INFO, '')
    log(INFO, '  > cd %s' % name)
    log(INFO, '  > auxilium test')
    log(INFO, '  > auxilium doc --api')
    log(INFO, '  > auxilium deploy')
    log(INFO, '  > auxilium doc --show')
    log(INFO, '')
    return 0
