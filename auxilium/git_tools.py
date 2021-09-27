# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from io import *
from logging import log, DEBUG, INFO, ERROR
from os import getcwd, linesep, chdir
from os.path import exists, join

from dulwich import porcelain
from dulwich.repo import Repo
from dulwich.errors import NotGitRepository


def commit_git(msg='', add='', path=getcwd()):
    """commit changes to local `git` repo"""
    cwd = getcwd()
    chdir(path)
    repo = Repo(path) if exists(join(path, '.git')) else Repo.init(path)
    if add:
        log(INFO,
            "*** adding all new files from %s to local `git` repo ***" % path)
        added, ignored = porcelain.add(repo)
        log(DEBUG, "added:")
        for p in added:
            log(DEBUG, "  %s" % p)
        for p in ignored:
            log(DEBUG, "ignored: %s" % p)

    msg = msg if msg else 'Commit'
    msg += ' (via auxilium)'
    log(INFO, "*** commit changes to local `git` repo at %s ***" % path)
    log(DEBUG, "msg: `%s`" % msg)
    porcelain.commit(repo, msg)
    chdir(cwd)
    return 0


def tag_git(tag, msg='', path=getcwd()):
    """tag current branch of local `git` repo"""
    log(INFO, "*** tag current branch of local `git` repo at %s ***" % path)
    log(DEBUG, "tag: `%s`" % tag)
    if msg:
        log(DEBUG, "msg: `%s`" % msg)
    porcelain.tag_create(Repo(path), tag, message=msg)
    return 0


def push_git(remote='None', path=getcwd()):
    """push current branch of local to remote `git` repo"""
    log(INFO, "*** push current branch of local "
              "to remote `git` repo at %s ***" % remote)
    if remote:
        log(DEBUG, "remote: `%s`" % str(remote))
    out, err = BytesIO(), BytesIO()
    try:
        porcelain.push(Repo(path), remote, outstream=out, errstream=err)
    except NotGitRepository as e:
        log(ERROR, e)
        return 1
    if out:
        for line in out.read().decode("utf-8").split(linesep):
            if line:
                log(DEBUG, line)
    if err:
        for line in err.read().decode("utf-8").split(linesep):
            if line:
                log(ERROR, line)
    return 0
