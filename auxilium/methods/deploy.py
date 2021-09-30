# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Thursday, 30 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import getcwd
from os.path import basename
from logging import log, ERROR

from ..tools.build_tools import build as _build, cleanup as _cleanup
from ..tools.const import ICONS
from ..tools.docmaintain_tools import docmaintain
from ..tools.git_tools import commit_git, tag_git, push_git
from ..tools.pypi_tools import deploy as _deploy


def do(pkg=basename(getcwd()), commit=None, tag=None, header=None,
       build=None, push=None, remote=None, remote_usr=None, remote_pwd=None,
       deploy=None, pypi_usr=None, pypi_pwd=None, cleanup=None,
       path=None, env=None, **kwargs):
    """run deploy process"""

    if cleanup:
        return _cleanup()

    build_return_code = -1
    code = False

    if header:
        code = code or docmaintain(pkg, path=path)

    if build:
        build_return_code = _build()
        code = code or build_return_code

    if commit:
        if build_return_code == 0:
            code = code or commit_git(commit)
        else:
            log(ERROR, ICONS["error"] +
                'build missing or failed . did not commit.')

    if tag:
        if build_return_code == 0:
            code = code or tag_git(tag, path=path)
        else:
            log(ERROR, ICONS["error"] +
                'build missing or failed . did not tag.')

    if push:
        if build_return_code == 0:
            url = remote.replace('https://', '')
            usr = remote_usr
            pwd = '' if remote_pwd == 'None' else ':' + remote_pwd  # nosec
            remote = 'https://' + usr + pwd + '@' + url
            code = code or push_git(remote, path)
        else:
            log(ERROR, ICONS["error"] +
                'build missing or failed . did not push.')

    if deploy:
        if build_return_code == 0:
            code = code or _deploy(pypi_usr, pypi_pwd)
        else:
            log(ERROR, ICONS["error"] +
                'build missing or failed . did not deploy.')

    return code
