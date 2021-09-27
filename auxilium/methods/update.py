# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import getcwd
from os.path import basename

from ..tools.pip_tools import upgrade, uninstall, cleanup as _cleanup, \
    requirements as _requirements, install as _install
from ..tools.git_tools import commit_git
from ..tools.docmaintain_tools import docmaintain


def do(pkg=basename(getcwd()), commit=None, add=None,
       install=None, requirements=None, doc_header=None, cleanup=None,
       path=getcwd(), env=None, **kwargs):
    code = False
    if cleanup:
        code = code or upgrade(path=path, venv=env)
        code = code or _cleanup(path=path, venv=env)
        code = code or uninstall(pkg, venv=env)
    else:
        if install:
            code = code or upgrade(path=path, venv=env)
            code = code or _install(path=path, venv=env)
        if requirements:
            code = code or upgrade(path=path, venv=env)
            code = code or _requirements(path=path, venv=env)
        if doc_header:
            code = code or docmaintain(pkg, path=path)
        if commit:
            code = code or commit_git(commit, add, path=path)
    return code