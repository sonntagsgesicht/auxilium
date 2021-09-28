#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
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
    """run test process"""

    if cleanup:
        return _cleanup(path)

    test_return_code = -1
    code = False

    if quality:
        code = code or _quality(pkg, venv=env)

    if security:
        code = code or _security(pkg, venv=env)

    if path:
        test_return_code = _test(path, venv=env)
        code = code or test_return_code

    if coverage and path:
        code = code or _coverage(pkg, path, venv=env)

    if commit:
        if test_return_code == 0:
            code = code or commit_git(commit)
        else:
            log(ERROR, "⚠️ Test missing or failed. Did not commit.")

    return code
