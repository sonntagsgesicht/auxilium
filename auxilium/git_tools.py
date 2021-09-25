# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, DEBUG, INFO
from os import getcwd
from os.path import exists, join

from dulwich import porcelain
from dulwich.repo import Repo


def commit_git(msg='', add='', path=getcwd()):
    """commit changes to local `git` repo"""
    repo = Repo(path) if exists(join(path, '.git')) else Repo.init(path)
    if add:
        log(INFO, "*** adding all new files to local `git` repo***")
        # add = add if isinstance(add, str) else '--all'
        added, ignored = porcelain.add(repo)
        for p in added:
            log(DEBUG, "added: %s" % p)
        for p in ignored:
            log(DEBUG, "ignored: %s" % p)

    msg = msg if msg else 'Commit'
    msg += ' (via auxilium)'
    log(INFO, "*** commit changes to local `git` repo ***")
    log(INFO, "msg: `%s`" % msg)
    porcelain.commit(repo, msg)
