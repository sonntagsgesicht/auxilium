# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from os import path, getcwd


def create(usr, pwd, pkg=path.basename(getcwd())):
    """create repo on bitbucket.com"""
    raise NotImplementedError()


def release(usr, pwd, pkg=path.basename(getcwd())):
    """draft release on github.com"""
    raise NotImplementedError()
