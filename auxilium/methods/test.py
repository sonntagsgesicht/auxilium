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
from logging import log, ERROR

from ..tools.test_tools import quality as _quality, security as _security, \
    test as _test, coverage as _coverage, cleanup as _cleanup
from ..tools.git_tools import commit_git


def do(pkg=basename(getcwd()), commit=None,
       quality=None, security=None, coverage=None, cleanup=None,
       path=None, env=None, **kwargs):
    res = list()
    if quality:
        res.append(_quality(pkg, venv=env))
    if security:
        res.append(_security(pkg, venv=env))
    if path:
        res.append(_test(path, venv=env))
        if coverage:
            res.append(_coverage(pkg, path, venv=env))
    code = any(res)
    if commit:
        if code:
            log(ERROR, "⚠️ Test missing or failed. Did not commit.")
        else:
            code = code or commit_git(commit)
    if cleanup:
        code = code or _cleanup(path)
    return code
