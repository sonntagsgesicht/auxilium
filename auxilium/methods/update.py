# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.9, copyright Sunday, 03 October 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import getcwd
from os.path import basename, exists, join

from ..tools.const import GIT_PATH
from ..tools.docmaintain_tools import docmaintain
from ..tools.dulwich_tools import commit_git, add_git, status_git, init_git, \
    pull_git, build_url
from ..tools.pip_tools import upgrade as _upgrade, uninstall, \
    rollback, requirements as _requirements, install as _install


def do(pkg=basename(getcwd()), header=None, commit=None, pull=None,
       remote=None, remote_usr=None, remote_pwd=None,
       install=None, upgrade=None, requirements=None, cleanup=None,
       path=getcwd(), env=None, **kwargs):
    if cleanup:
        return uninstall(pkg, venv=env) or rollback(path=path, venv=env)

    code = False
    if header:
        code = code or docmaintain(pkg, path=path)
    if commit:
        if not exists(join(path, GIT_PATH)):
            code = code or init_git(path=path, venv=env)
        code = code or add_git(path=path, venv=env)
        code = code or status_git(path=path, venv=env)
        code = code or commit_git(commit, path=path, venv=env)
    if pull:
        remote = build_url(remote, remote_usr, remote_pwd)
        code = code or pull_git(
            remote=remote, path=path, venv=env)
    if upgrade:
        code = code or _upgrade(upgrade, path=path, venv=env)
    if install:
        code = code or _install(path=path, venv=env)
    if requirements:
        code = code or _requirements(path=path, venv=env)

    return code
