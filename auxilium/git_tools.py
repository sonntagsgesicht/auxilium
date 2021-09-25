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


from logging import log, INFO

from .system_tools import system


def create_git(path='.'):
    """create local `git` repo"""
    log(INFO, "create local `git` repo")
    if system("git --version", level=0) == 0:
        system('git init .', path=path)
        commit_git('Initial commit', add='--all', path=path)


def commit_git(msg='', add='', path='.'):
    """commit changes to local `git` repo"""
    log(INFO, "commit changes to local `git` repo")
    if system("git --version", level=0) == 0:
        if add:
            log(INFO, "first adding all new files")
            if isinstance(add, str):
                system('git add %s' % add, path=path)
            else:
                system('git add --all', path=path)
        if not msg:
            msg = 'Commit'
        msg += ' (via auxilium)'
        system('git commit -m "%s"' % msg, path=path)
