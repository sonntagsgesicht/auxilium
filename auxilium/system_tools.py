from logging import log, DEBUG, INFO, ERROR
from os import linesep, getcwd, name as os_name, remove
from os.path import basename, exists, isdir
from shutil import rmtree
from sys import executable

from subprocess import run

PYTHON = executable
VENV_PATH = '.aux/venv'


def create_venv(pkg=basename(getcwd()),
                venv_path=VENV_PATH,
                path=getcwd()):
    """create virtual python environment"""
    log(INFO, "create virtual environment at %s" % venv_path)
    module('venv', "--prompt %s %s" % (pkg, venv_path), path=path)


def activate_venv(venv_path=VENV_PATH):
    """activate virtual python environment"""
    if os_name == 'nt':
        log(INFO, "activate virtual environment at %s" % venv_path)
        return "C:\\> %s\\Scripts\\activate.bat; " % venv_path
    elif os_name == 'posix':
        log(INFO, "activate virtual environment at %s" % venv_path)
        return "source %s/bin/activate; " % venv_path
    else:
        log(INFO, "unable to activate virtual environment for os %s" % os_name)


def system(command, level=DEBUG, path=getcwd(), venv=None):
    log(level, "call `%s` in %s" % (command, path))
    if venv:
        command = activate_venv() + command
    proc = run(command, cwd=path, shell=True, capture_output=True, text=True)
    if proc.stdout:
        for line in str(proc.stdout).split(linesep):
            if line:
                log(level, line)
    if proc.stderr:
        for line in str(proc.stderr).split(linesep):
            if line:
                log(level, line)
    return proc.returncode


def python(command, level=DEBUG, path=getcwd(), venv=PYTHON):
    return system(venv + ' ' + command, level, path)


def module(mdl, command='', level=DEBUG, path=getcwd(), venv=PYTHON):
    mdl = getattr(mdl, '__name__', str(mdl))
    return python(' -m ' + mdl + ' ' + command, level, path, venv)


def del_tree(*paths, level=DEBUG):
    for f in paths:
        if exists(f):
            if isdir(f):
                log(level, 'remove tree below %s' % f)
                rmtree(f)
            else:
                log(level, 'remove file %s' % f)
                remove(f)

