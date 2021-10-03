# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.9, copyright Sunday, 03 October 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, DEBUG, INFO, ERROR
from os import getcwd, chdir
from os.path import exists, join, sep

from .const import ICONS
from .setup_tools import EXT
from .system_tools import script

try:
    from dulwich import porcelain
    from dulwich.repo import Repo
except ImportError as e:
    dulwich_msg = 'import dulwich failed - git will not work'
    log(ERROR, ICONS["error"] + dulwich_msg)
    log(ERROR, ICONS[""] + str(e))


    def porcelain(*args, **kwargs):
        log(ERROR, ICONS["error"] + dulwich_msg)


    Repo = porcelain

BRANCH = 'master'
IMP = "from sys import exit", \
      "from dulwich.repo import Repo", \
      "from dulwich.porcelain import add, commit, status, tag_list, tag_create, push, log"


def git_cmd(cmd):
    return '"%s %s"' % (IMP, cmd)


def git_exit(cmd):
    return git_cmd("exit(%s)" % cmd)


def git_print(cmd):
    return git_cmd("print(%s)" % cmd)


def add_git(path=getcwd(), venv=None):
    """add files to local `git` repo"""
    script("print(adding str(status().unstaged))",
           imports=IMP, level=INFO, path=path, venv=venv)
    return script("exit(Repo('.').stage(status().unstaged))",
                  imports=IMP, level=INFO, path=path, venv=venv)


def status_git(path=getcwd(), venv=None):
    """get status of local `git` repo"""
    log(INFO, ICONS["status"] + "file status in local `git` repo")
    log(DEBUG, ICONS[""] + "at " + path)
    script(
        "print('add       : ' + ', '.join(map(str, status().staged['add'])))",
        imports=IMP, level=INFO, path=path, venv=venv)
    script(
        "print('delete    : ' + ', '.join(map(str, status().staged['delete'])))",
        imports=IMP, level=INFO, path=path, venv=venv)
    script(
        "print('modify    : ' + ', '.join(map(str, status().staged['modify'])))",
        imports=IMP, level=INFO, path=path, venv=venv)
    script("print('unstaged  : ' + ', '.join(map(str, status().unstaged)))",
           imports=IMP, level=INFO, path=path, venv=venv)
    script("print('untracked : ' + ', '.join(map(str, status().untracked)))",
           imports=IMP, level=INFO, path=path, venv=venv)


def commit_git(msg='', path=getcwd(), venv=None):
    """commit changes to local `git` repo"""
    status_git(path=path, venv=venv)
    add_git(path=path, venv=venv)
    msg = (msg if msg else 'Commit') + EXT
    log(INFO, ICONS["commit"] + "commit changes to local `git` repo")
    log(DEBUG, ICONS[""] + "at " + path)
    return script("print('[' + (commit(message=%r)).decode()[:6] + '] ' + %r)"
                  % (msg, msg), imports=IMP, level=INFO, path=path, venv=venv)


def tag_git(tag, msg='few', path=getcwd(), venv=None):
    """tag current branch of local `git` repo"""
    tag_exists = script("exit(%r in tag_list('.'))" % bytearray(tag.encode()),
                        imports=IMP, level=INFO, path=path, venv=venv)
    if tag_exists:
        log(ERROR, ICONS["error"] +
            "tag %r exists in current branch of local `git` repo" % tag)
        return 1
    log(INFO, ICONS["tag"] + "tagging last commit")
    log(DEBUG, ICONS[""] + "at " + path)

    script("print('tag:    %s')" % tag,
           imports=IMP, level=INFO, path=path, venv=venv)
    if msg:
        script("print('message: %s')" % msg,
               imports=IMP, level=INFO, path=path, venv=venv)
    script("print(log(max_entries=1))",
           imports=IMP, level=INFO, path=path, venv=venv)
    return script("exit(tag_create('.', tag=%r, message=%r))" % (tag, msg),
                  imports=IMP, level=INFO, path=path, venv=venv)


def build_url(url, usr='', pwd='None'):  # nosec
    pwd = ':' + str(pwd) if pwd and pwd != 'None' else ''
    usr = str(usr) if usr else 'token-user' if pwd else ''
    remote = \
        'https://' + usr + pwd + '@' + url.replace('https://', '')
    return remote


def clean_url(url):
    http, last = url.split('//', 1)
    usr_pwd, url = last.split('@', 1)
    usr, _ = usr_pwd.split(':', 1) if ':' in usr_pwd else (usr_pwd, '')
    return http + '//' + usr + '@' + url


def push_git(remote='None', branch=BRANCH, path=getcwd(), venv=None):
    """push current branch of local to remote `git` repo"""
    log(INFO, ICONS["push"] + "push current branch to remote `git` repo")
    log(DEBUG, ICONS[""] + "at " + clean_url(remote))
    return script("push('.', %s, %s)" % (remote, branch),
                  imports=IMP, level=INFO, path=path, venv=venv)
