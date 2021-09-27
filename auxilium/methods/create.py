# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import getcwd, chdir
from os.path import basename
from sys import path as sys_path

from ..tools.setup_tools import create_project, create_finish
from ..tools.system_tools import create_venv
from ..tools.git_tools import commit_git
from ..tools.pip_tools import upgrade, install, requirements
from ..tools.docmaintain_tools import docmaintain


def do(name=None, slogan=None, author=None, email=None, url=None,
       commit=None, path=getcwd(), venv=None, env=None, **kwargs):
    pkg_path = create_project(name, slogan, author, email, url, path=path)
    pkg = basename(pkg_path)
    code = int(not pkg_path.endswith(name)) if name else 0

    chdir(pkg_path)
    sys_path.append(pkg_path)

    if venv:
        # create virtual environment
        # venv = venv.replace('bin/python3')
        env = create_venv(pkg, venv_path=venv, path=pkg_path, venv=env)
        # run default update command
        code = code or upgrade(path=pkg_path, venv=env)
        code = code or install(path=pkg_path, venv=env)
        code = code or requirements(path=pkg_path, venv=env)
        code = code or docmaintain(pkg, path=pkg_path)

    if commit:
        # init git repo with initial commit
        code = code or commit_git(commit, path=pkg_path)

    code = code or create_finish(pkg)
    return code
