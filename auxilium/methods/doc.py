# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.9, copyright Sunday, 03 October 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, ERROR
from os import getcwd
from os.path import basename

from ..tools.const import ICONS
from ..tools.dulwich_tools import commit_git
from ..tools.sphinx_tools import api as _api, doctest as _doctest, \
    html as _html, latexpdf as _pdf, show as _show, cleanup as _cleanup

DID_NOT_COMMIT = 'doctest or build missing - did not commit'


def do(pkg=basename(getcwd()), commit=None, fail_fast=None, pdf=None,
       api=None, doctest=None, html=None, show=None, cleanup=None,
       path=None, env=None, **kwargs):
    if cleanup:
        return _cleanup(env)

    code = False
    if api:
        code = code or _cleanup(path=path, venv=env)
        code = code or _api(pkg=pkg, path=path, venv=env)
    if doctest:
        code = code or _doctest(fail_fast=fail_fast, path=path, venv=env)
    if html:
        code = code or _html(fail_fast=fail_fast, path=path, venv=env)
    if pdf:
        code = code or _pdf(fail_fast=fail_fast, path=path, venv=env)
    if commit:
        if doctest and html:
            code = code or commit_git(commit)
        else:
            log(ERROR, ICONS["error"] + DID_NOT_COMMIT)
            code = True
    if show:
        code = code or _show(env)
    return code
