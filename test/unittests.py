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


import datetime
import logging
import os
import sys
import unittest

from dulwich.porcelain import tag_list, status

from auxilium.tools.const import DEMO_PATH, TEST_LOG_FORMATTER, ICONS
from auxilium.tools.system_tools import module, del_tree
from auxilium.tools.dulwich_tools import init_git, status_git, add_git, \
    tag_git, push_git, pull_git, clone_git, branch_git, \
    checkout_git, add_and_commit_git

sys.path.append('..')

CWD, _ = os.path.split(__file__)

logging.basicConfig(level=logging.INFO, format=TEST_LOG_FORMATTER)

# set icons set on windows machine
if not os.name == 'posix':
    ICONS.clear()
    ICONS.update({'error': '!!', 'warn': '!'})


def auxilium(command, level=logging.INFO, path=None):
    return module('auxilium', command, level=level, path=path)


class AuxiliumUnitTests(unittest.TestCase):

    def setUp(self):
        logging.log(logging.INFO, '')
        logging.log(logging.INFO, ICONS['test'] + 'start unittests')
        self.wdir = os.path.join(CWD, 'working_dir')
        self.level = ''
        if not os.path.exists(self.wdir):
            os.mkdir(self.wdir)
        os.chdir(self.wdir)

    def tearDown(self):
        try:
            del_tree(self.wdir)
        except PermissionError:
            pass

    def assertReturns(self, expected_return, function, *args, **kwargs):
        actual_return = function(*args, **kwargs)
        return self.assertEqual(expected_return, actual_return)

    def assertReturnsZero(self, function, *args, **kwargs):
        actual_return = function(*args, **kwargs)
        return self.assertFalse(bool(actual_return), str(actual_return))

    def assertReturnsNonZero(self, function, *args, **kwargs):
        actual_return = function(*args, **kwargs)
        return self.assertTrue(bool(actual_return), str(actual_return))


class CreateRepoUnitTests(AuxiliumUnitTests):

    def test_auxilium_demo(self):
        path = os.path.join(self.wdir, DEMO_PATH)
        del_tree(path)
        self.assertEqual(0, auxilium('%s --demo' % self.level, path=self.wdir))

        self.assertEqual(0, auxilium('%s update' % self.level, path=path))
        self.assertEqual(0, auxilium('%s test --fail-fast' % self.level,
                                     path=path))

        self.assertEqual(0, auxilium('%s doc --api --fail-fast' % self.level,
                                     path=path))
        self.assertEqual(0, auxilium('%s build' % self.level, path=path))

        self.assertEqual(0, auxilium('%s build --tag' % self.level, path=path))
        self.assertNotEqual(0, auxilium('%s build --tag' % self.level,
                                        path=path))
        self.assertNotEqual(0, auxilium('%s test --fail-fast --coverage=99'
                                        % self.level, path=path))

        del_tree(path)

    def test_unicorn(self):
        name, doc, author = 'unicorn', 'Always be a unicorn.', 'dreamer'
        email, url = '<name>@home', 'https://<author>.home/<name>'
        inputs = name, doc, author, email, url

        path = os.path.join(self.wdir, name)
        del_tree(path)

        file_path = os.path.join(self.wdir, name + '_details')
        with open(file_path, "w") as f:
            f.write(os.linesep.join(inputs))
        self.assertEqual(0, auxilium('%s create < %s' %
                                     (self.level, file_path), path=self.wdir))
        self.assertEqual(0, auxilium('%s update' % self.level, path=path))
        self.assertEqual(0, auxilium('%s test --fail-fast' % self.level,
                                     path=path))
        self.assertEqual(0, auxilium('%s doc --fail-fast --api' % self.level,
                                     path=path))
        self.assertEqual(0, auxilium('%s build' % self.level, path=path))
        del_tree(path)


class AuxiliumMethodTests(AuxiliumUnitTests):

    def testDulwich(self):

        # init remote and repo dir

        remote = os.path.join(self.wdir, 'git_remote')
        if os.path.exists(remote):
            del_tree(remote)
        os.mkdir(remote)

        path = os.path.join(self.wdir, 'git_test')
        if os.path.exists(path):
            del_tree(path)
        os.mkdir(path)

        # start at remote

        self.assertReturnsNonZero(status_git, path=remote)

        self.assertReturnsZero(init_git, path=remote)
        first_file = 'first_file'
        first_contents = 'Hello to repo!'
        with open(os.path.join(remote, first_file), 'w') as file:
            file.write(first_contents)
        self.assertIn(first_file, status(remote).untracked)

        self.assertReturnsZero(add_git, path=remote)
        self.assertIn(first_file.encode(), status(remote).staged['add'])

        self.assertReturnsZero(add_and_commit_git,
                               'remote_commit', path=remote)

        self.assertReturnsZero(branch_git, 'other', path=remote)

        if os.name == 'posix':
            self.assertReturnsZero(checkout_git, 'other', path=remote)

        # switch to repo

        self.assertReturnsZero(clone_git, remote, path=path)
        if os.name == 'posix':
            self.assertReturnsZero(checkout_git, 'master', path=path)

        self.assertReturnsZero(pull_git, remote, path=path)
        self.assertReturnsZero(add_and_commit_git, 'empty_commit', path=path)

        with open(os.path.join(path, 'first_file'), 'r') as file:
            read_first_contents = file.read()
        self.assertEqual(first_contents, read_first_contents)

        append_contents = ' And hello to remote!'
        with open(os.path.join(path, first_file), 'a') as file:
            file.write(append_contents)

        second_contents = 'Hello to remote!'
        second_file = 'second_file'
        with open(os.path.join(path, second_file), 'w') as file:
            file.write(second_contents)

        self.assertIn(first_file.encode(), status(path).unstaged)
        self.assertIn(second_file, status(path).untracked)

        self.assertReturnsZero(status_git, path=path)

        self.assertReturnsZero(add_git, path=path)

        self.assertReturnsZero(status_git, path=path)

        self.assertIn(first_file.encode(), status(path).staged['modify'])
        self.assertIn(second_file.encode(), status(path).staged['add'])

        self.assertReturnsZero(add_and_commit_git, 'repo_commit', path=path)

        tag = 'test_tag'
        self.assertReturnsZero(tag_git, tag, path=path)
        self.assertIn(tag.encode(), tag_list(path))

        self.assertReturnsZero(push_git, remote, path=path)

        # switch back to remote

        if os.name == 'posix':
            self.assertReturnsZero(checkout_git, 'master', path=remote)

            with open(os.path.join(remote, first_file), 'r') as file:
                self.assertEqual(file.read(), first_contents + append_contents)
            with open(os.path.join(remote, second_file), 'r') as file:
                self.assertEqual(file.read(), second_contents)


if __name__ == "__main__":
    start_time = datetime.datetime.now()

    print('')
    print('=' * 80)
    print('')
    print(('run %s' % __file__))
    print(('in %s' % os.getcwd()))
    print(('started  at %s' % str(start_time)))
    print('')
    print('-' * 80)
    print('')

    unittest.main(verbosity=2)

    print('')
    print('=' * 80)
    print('')
    print(('ran %s' % __file__))
    print(('in %s' % os.getcwd()))
    print(('started  at %s' % str(start_time)))
    print(('finished at %s' % str(datetime.datetime.now())))
    print('')
    print('-' * 80)
    print('')
