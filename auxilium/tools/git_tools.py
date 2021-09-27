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
    """add and commit changes to local `git` repo"""
    cwd = getcwd()
    chdir(path)
    repo = Repo(path) if exists(join(path, '.git')) else Repo.init(path)
    _, files, _ = porcelain.status(repo)
    repo.stage(files)
    # added, ignored = porcelain.add(repo)
    log(INFO, "*** file status in `git` repo")
    log(INFO, "    from " + path)
    staged, un_staged, untracked = porcelain.status(repo, False)
    if staged['add']:
        log(INFO, "    add:")
        for p in staged['add']:
            log(INFO, "      %s" % p.decode())
    if staged['modify']:
        log(INFO, "    modify:")
        for p in staged['modify']:
            log(INFO, "      %s" % p.decode())
    if staged['delete']:
        log(INFO, "    delete:")
        for p in staged['delete']:
            log(INFO, "      %s" % p.decode())
    for p in un_staged:
        log(INFO, "    unstaged: %s" % p.decode())
    for p in untracked:
        log(INFO, "    untracked : %s" % p)
    msg = msg if msg else 'Commit'
    msg += ' (via auxilium)'
    log(INFO, "*** commit changes as `%s`" % msg)
    log(INFO, "    at " + path)
    res = porcelain.commit(repo, msg)
    log(INFO, "    as %s" % res.decode())

    chdir(cwd)
    return 0


def tag_git(tag, msg='', path=getcwd()):
    """tag current branch of local `git` repo"""
    log(INFO, "*** tag current branch as %s" % tag)
    log(INFO, "    at " + path)
    if bytearray(tag.encode()) in porcelain.tag_list(Repo(path)):
        log(ERROR, "⚠️ Tag %s exists in current branch of local `git` repo" % tag)
        return 1

    if msg:
        log(DEBUG, "    msg: `%s`" % msg)
    porcelain.tag_create(Repo(path), tag, message=msg)
    return 0


def push_git(remote='None', path=getcwd()):
    """push current branch of local to remote `git` repo"""
    log(INFO, "*** push current branch to remote `git` repo")
    log(INFO, "    at " + remote)
    if remote:
        log(DEBUG, "    remote: `%s`" % str(remote))
    out, err = BytesIO(), BytesIO()
    try:
        porcelain.push(Repo(path), remote, 'master',
                       outstream=out, errstream=err)
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
