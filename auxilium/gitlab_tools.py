

from os import path, getcwd


def create(usr, pwd, pkg=path.basename(getcwd())):
    """create repo on gitlab.com"""
    raise NotImplementedError()


def release(usr, pwd, pkg=path.basename(getcwd())):
    """draft release on github.com"""
    raise NotImplementedError()
