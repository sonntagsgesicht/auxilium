# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, DEBUG, INFO, ERROR
from os import linesep, getcwd, name as os_name, remove
from os.path import basename, exists, isdir, join, normpath
from shutil import rmtree
from subprocess import run, Popen, PIPE, STDOUT  # nosec
from sys import executable

from .const import PYTHON, VENV_PATH, VENV_TAIL, SUB_FORMATTER_PREFIX


def create_venv(pkg=basename(getcwd()),
                venv_path=VENV_PATH,
                path=getcwd(),
                venv=None):
    """create virtual python environment"""
    # check if venv exists
    venv = venv if venv and exists(venv) else None
    # strip potential executable from venv_path
    venv_path = venv_path.replace(VENV_TAIL, '')
    log(INFO, "👻  create virtual environment")
    module('venv', "--clear --prompt %s %s" % (pkg, venv_path),
           path=path, venv=venv)
    return join(venv_path, VENV_TAIL)


def activate_venv(venv_path=VENV_PATH):
    """activate virtual python environment"""
    # strip potential executable from venv_path
    venv_path = venv_path.replace(VENV_TAIL, '')
    if os_name == 'nt':
        log(DEBUG, "    activate virtual environment at %s" % venv_path)
        return join(venv_path, 'Scripts', 'activate.bat')
    elif os_name == 'posix':
        log(DEBUG, "    activate virtual environment at %s" % venv_path)
        return "source %s; " % join(venv_path, 'bin', 'activate')
    else:
        log(ERROR,
            "    unable to activate virtual environment for os %s" % os_name)


def shell(command, level=DEBUG, path=getcwd(), venv=None,
          capture_output=True):
    log(DEBUG, "    >>> %s" % command)
    log(DEBUG, "    in %s" % path)
    if venv:
        command = activate_venv(venv) + ' ' + command
    return _popen(command, level, path)


def _popen(command, level=DEBUG, path=getcwd()):
    proc = Popen(
        command,
        stdout=PIPE,
        stderr=STDOUT,
        universal_newlines=True,
        cwd=path, shell=True, text=True)  # nosec
    for stdout_line in iter(proc.stdout.readline, ""):
        log(level, "    " + SUB_FORMATTER_PREFIX + " " + stdout_line.rstrip())
    proc.stdout.close()
    return proc.wait()


def _run(command, level=DEBUG, path=getcwd()):
    proc = run(
        command, cwd=path, shell=True, capture_output=True, text=True)  # nosec
    log_level = ERROR if proc.returncode else level
    if proc.stdout:
        for line in str(proc.stdout).split(linesep):
            if line:
                log(log_level, line)
    if proc.stderr:
        for line in str(proc.stderr).split(linesep):
            if line:
                log(log_level, line)
    return proc.returncode


def python(command, level=DEBUG, path=getcwd(), venv=None,
           capture_output=True):
    venv = venv if venv else PYTHON
    return shell(venv + ' ' + command, level, path,
                 capture_output=capture_output)


def module(mdl, command='', level=DEBUG, path=getcwd(), venv=None):
    mdl = getattr(mdl, '__name__', str(mdl))
    return python('-m ' + mdl + ' ' + command, level, path, venv)


def del_tree(*paths, level=DEBUG):
    for f in paths:
        if exists(f):
            if isdir(f):
                log(level, 'remove tree below %s' % f)
                rmtree(f)
            else:
                log(level, 'remove file %s' % f)
                remove(f)
    return 0
