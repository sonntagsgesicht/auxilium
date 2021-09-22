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
from logging import log, INFO, basicConfig
from os import remove, system, path, getcwd, sep, walk, makedirs, \
    name as os_name
from shutil import move
from zipfile import ZipFile

basicConfig()

PYTHON = 'python3'
VENV_PATH = '.aux/venv'


def create_project(name=None, slogan=None, author=None, email=None):
    """create a new python project with auxilium"""
    loc = __file__.split(sep)
    loc[-1] = sep.join(('data', 'pkg.zip'))
    loc = sep.join(loc)

    log(INFO, 'Please enter project details.\n')

    name = input('Enter project name  : ') if name is None else name
    slogan = input('Enter project slogan: ') if slogan is None else slogan
    author = input('Enter author name   : ') if author is None else author
    email = input('Enter author email  : ') if email is None else email

    root_path = getcwd() + sep + name
    pkg_path = root_path + sep + name

    # setup project infrastructure
    if path.exists(root_path):
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
            log(INFO, '  ' + path.join(subdir, file))

    log(INFO, '')
    log(INFO, "Consider a first full run via: 'cd %s; auxilium full;'" % name)
    log(INFO, '')


def create_venv(pkg=path.basename(getcwd()), venv_path=VENV_PATH, python=PYTHON):
    """create virtual python environment"""
    log(INFO, "create virtual environment at %s" % venv_path)
    system(python + " -m venv --prompt %s %s" % (pkg, venv_path))


def create_git(pkg=path.basename(getcwd())):
    """create local `git` repo"""
    system('git init .')
    system('git add --all')
    system('git commit -m "Initial commit (via auxilium)"')


def commit_git(msg='commit (via auxilium)', git_all=False):
    """commit changes to local `git` repo"""
    if git_all:
        system('git add --all')
    system('git commit -m %s' % msg)


def activate_venv(venv_path=VENV_PATH):
    """activate virtual python environment"""
    if os_name == 'nt':
        log(INFO, "activate virtual environment at %s" % venv_path)
        # "PS C:\\> %s\\Scripts\\Activate.ps1" % venv_path  # pwr_shell
        system("C:\\> %s\\Scripts\\activate.bat" % venv_path)
    elif os_name == 'posix':
        log(INFO, "activate virtual environment at %s" % venv_path)
        system("source %s/bin/activate" % venv_path)
    else:
        log(INFO, "unable to activate virtual environment for os %s" % os_name)


def requirements(python=PYTHON):
    """manage requirements (dependencies) in `requirements.txt`
        and `upgrade_requirements.txt`"""
    log(INFO, '*** setup environment requirements ***')
    system(python + " -m pip freeze > freeze_requirements.txt")
    if path.exists("requirements.txt"):
        system(python + " -m pip install -r requirements.txt")
    if path.exists("upgrade_requirements.txt"):
        system(python + " -m pip install --upgrade -r upgrade_requirements.txt")


def install(python=PYTHON):
    """install current project via `pip install -e .`"""
    log(INFO, '*** install project via pip install -e ***')
    system(python + " -m pip install --upgrade -e .")
    log(INFO, '')


def uninstall(pkg=path.basename(getcwd()), python=PYTHON):
    """uninstall current project via `pip uninstall`"""
    log(INFO, '*** uninstall project via pip uninstall ***')
    system(python + " -m pip uninstall -y %s" % pkg)


def cleanup(python=PYTHON):
    """remove temporary files"""
    log(INFO, '*** clean environment ***')
    if 0 or path.exists("freeze_requirements.txt"):
        if path.exists("requirements.txt"):
            system(python + " -m pip uninstall -y -r requirements.txt")
        if path.exists("upgrade_requirements.txt"):
            system(python + " -m pip uninstall -y -r upgrade_requirements.txt")
        system(python + " -m pip install --upgrade -r freeze_requirements.txt")
        remove("freeze_requirements.txt")
