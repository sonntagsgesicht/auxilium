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
from .system_tools import command

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
IMP = "from sys import exit as e; " \
      "from dulwich.repo import Repo; " \
      "from dulwich.porcelain import " \
      "add, commit, status, tag_list, tag_create, push; "


def push(remote, branch=BRANCH):
    return


def add_git(path=getcwd(), venv=None):
    cwd = getcwd()
    chdir(path)
    repo = Repo(path) if exists(join(path, '.git')) else Repo.init(path)
    _, files, untracked = porcelain.status(repo)
    repo.stage(files)
    repo.stage(untracked)
    added, ignored = porcelain.add(repo)
    staged, un_staged, untracked = porcelain.status(repo, False)
    if not any(staged.values()):
        log(INFO, ICONS["missing"] + "not files found - did not commit")
        log(DEBUG, ICONS[""] + "at " + path)
        chdir(cwd)
        return 0

    log(INFO, ICONS["status"] + "file status in `git` repo")
    log(DEBUG, ICONS[""] + "at " + path)

    def paths_sorted(paths):
        sorted_file_paths = sorted(x for x in paths if sep not in str(x))
        sorted_sub_path = sorted(x for x in paths if sep in str(x))
        return sorted_file_paths + sorted_sub_path

    if staged['add']:
        log(INFO, ICONS[""] + "add:")
        for p in paths_sorted(staged['add']):
            log(INFO, ICONS[""] + "  %s" % p.decode())
    if staged['modify']:
        log(INFO, ICONS[""] + "modify:")
        for p in paths_sorted(staged['modify']):
            log(INFO, ICONS[""] + "  %s" % p.decode())
    if sorted(staged['delete']):
        log(INFO, ICONS[""] + "delete:")
        for p in paths_sorted(staged['delete']):
            log(INFO, ICONS[""] + "  %s" % p.decode())
    for p in paths_sorted(un_staged):
        log(INFO, ICONS[""] + "unstaged: %s" % p.decode())
    for p in paths_sorted(untracked):
        log(INFO, ICONS[""] + "untracked : %s" % p)
    chdir(cwd)
    return 0


def git_cmd(cmd):
    return '"%s print(%s)"' % (IMP, cmd)


def commit_git(msg='', path=getcwd(), venv=None):
    """add and commit changes to local `git` repo"""
    if command(git_cmd("Repo('.').stage(status().unstaged)"),
               level=DEBUG, path=path, venv=venv):
        return 1
    command(git_cmd("add      : status().staged['add']"), level=INFO, path=path, venv=venv)
    command(git_cmd("modified : status().staged['modified']"), level=INFO, path=path, venv=venv)
    command(git_cmd("deleted  : status().staged['deleted']"), level=INFO, path=path, venv=venv)
    command(git_cmd("unstaged : status().unstaged"), level=INFO, path=path, venv=venv)
    msg = (msg if msg else 'Commit') + EXT
    log(INFO, ICONS["commit"] + "commit changes as `%s`" % msg)
    log(DEBUG, ICONS[""] + "at " + path)
    return command(git_cmd("commit(message=%r)" % msg),
                   level=INFO, path=path, venv=venv)


def tag_git(tag, msg='', path=getcwd(), venv=None):
    """tag current branch of local `git` repo"""
    log(INFO, ICONS["tag"] + "current tags in local branch")
    tag_exists = command(git_cmd("e(%r in tag_list('.'))" %
                                 bytearray(tag.encode())),
                         level=INFO, path=path, venv=venv)
    if tag_exists:
        log(ERROR, ICONS["error"] +
            "tag %s exists in current branch of local `git` repo" % tag)
        return 1
    log(INFO, ICONS["tag"] + "tag current branch as %s" % tag)
    log(DEBUG, ICONS[""] + "at " + path)
    if msg:
        log(DEBUG, ICONS[""] + "msg: `%s`" % msg)
    return command(git_cmd("tag_create('.', tag=%r, message=%r)" %
                           (tag, msg)), level=INFO, path=path, venv=venv)


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


class Buffer(list):

    def write(self, b):
        self.append(b)


def push_git(remote='None', branch=BRANCH, path=getcwd(), venv=None):
    """push current branch of local to remote `git` repo"""
    log(INFO, ICONS["push"] + "push current branch to remote `git` repo")
    log(DEBUG, ICONS[""] + "at " + clean_url(remote))

    cmd = IMP + "push('.', %s, %s)" % (remote, branch)
    return command(cmd, level=INFO, path=path, venv=venv)

    try:
        out = Buffer()
        porcelain.push(Repo(path), remote, branch, out, out)
        for line in out:
            log(INFO, ICONS[""] + line.decode().strip())
            return 0
    except Exception as e:
        log(ERROR, ICONS['error'] + str(e))
        return 1
