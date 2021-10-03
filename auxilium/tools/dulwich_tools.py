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
IMP = "from sys import exit; " \
      "from dulwich.repo import Repo; " \
      "from dulwich.porcelain import " \
      "add, commit, status, tag_list, tag_create, push, log; "


def push(remote, branch=BRANCH):
    return


def _add_git(path=getcwd(), venv=None):
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
    return '"%s %s"' % (IMP, cmd)


def git_exit(cmd):
    return git_cmd("exit(%s)" % cmd)


def git_print(cmd):
    return git_cmd("print(%s)" % cmd)


def git_echo(cmd):
    return git_cmd("echo $(%s)") % cmd


def add_git(path=getcwd(), venv=None):
    """add files to local `git` repo"""
    command(git_print(
        "adding str(status().unstaged)"
    ), level=INFO, path=path, venv=venv)
    return command(git_exit(
            "Repo('.').stage(status().unstaged)"
    ), level=DEBUG, path=path, venv=venv)


def status_git(path=getcwd(), venv=None):
    """get status of local `git` repo"""
    log(INFO, ICONS["status"] + "file status in local `git` repo")
    log(DEBUG, ICONS[""] + "at " + path)
    command(git_print(
        "'add       : ' + ', '.join(map(str, status().staged['add']))"
    ),
        level=INFO, path=path, venv=venv)
    command(git_print(
        "'delete    : ' + ', '.join(map(str, status().staged['delete']))"
    ),
        level=INFO, path=path, venv=venv)
    command(git_print(
        "'modify    : ' + ', '.join(map(str, status().staged['modify']))"
    ),
        level=INFO, path=path, venv=venv)
    command(git_print(
        "'unstaged  : ' + ', '.join(map(str, status().unstaged))"
    ),
        level=INFO, path=path, venv=venv)
    command(git_print(
        "'untracked : ' + ', '.join(map(str, status().untracked))"
    ),
        level=INFO, path=path, venv=venv)


def commit_git(msg='', path=getcwd(), venv=None):
    """commit changes to local `git` repo"""
    status_git(path=path, venv=venv)
    msg = (msg if msg else 'Commit') + EXT
    log(INFO, ICONS["commit"] + "commit changes to local `git` repo")
    log(DEBUG, ICONS[""] + "at " + path)
    return command(git_print(
        "'[' + (commit(message=%r)).decode()[:6] + '] ' + %r" % (msg, msg)
    ), level=INFO, path=path, venv=venv)


def tag_git(tag, msg='few', path=getcwd(), venv=None):
    """tag current branch of local `git` repo"""
    tag_exists = command(git_exit(
        "%r in tag_list('.')" % bytearray(tag.encode())
    ), level=INFO, path=path, venv=venv)
    if tag_exists:
        log(ERROR, ICONS["error"] +
            "tag %r exists in current branch of local `git` repo" % tag)
        return 1
    log(INFO, ICONS["tag"] + "tagging last commit")
    log(DEBUG, ICONS[""] + "at " + path)

    command(git_print(
        "'tag:    %s'" % tag
    ), level=INFO, path=path, venv=venv)
    if msg:
        command(git_print(
            "'message: %s'" % msg
        ), level=INFO, path=path, venv=venv)
    command(git_print(
        "log(max_entries=1)"
    ), level=INFO, path=path, venv=venv)
    return command(git_cmd(
        "tag_create('.', tag=%r, message=%r)" % (tag, msg)
    ), level=INFO, path=path, venv=venv)


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
