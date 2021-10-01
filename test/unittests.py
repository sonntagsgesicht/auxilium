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

from auxilium.tools.const import DEMO_PATH
from auxilium.tools.system_tools import module, del_tree

sys.path.append('..')

CWD, _ = os.path.split(__file__)

log_format = "• %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)


def auxilium(command, path=None):
    return module('auxilium', command, path=path)


class CreateRepoUnitTests(unittest.TestCase):
    def setUp(self):
        logging.log(logging.INFO, '')
        logging.log(logging.DEBUG, 'start unittests')
        self.wdir = os.path.join(CWD, 'working_dir')
        self.name = 'unicorn'
        self.doc = 'Always be a unicorn.'
        self.author = 'dreamer'
        self.email = '<name>@home'
        self.url = 'https://<author>.home/<name>'
        if not os.path.exists(self.wdir):
            os.mkdir(self.wdir)
        os.chdir(self.wdir)

    def tearDown(self):
        try:
            del_tree(self.wdir)
        except:
            pass

    def test_auxilium_demo(self):
        path = os.path.join(self.wdir, DEMO_PATH)
        del_tree(path)
        self.assertEqual(0, auxilium('-vv -demo', path=self.wdir))
        self.assertEqual(0, auxilium('-vv update', path=path))
        self.assertEqual(0, auxilium('-vv test', path=path))
        self.assertEqual(0, auxilium('-vv doc --api', path=path))
        self.assertEqual(0, auxilium('-vv build', path=path))

        self.assertEqual(0, auxilium('-vv build --tag', path=path))
        self.assertNotEqual(0, auxilium('-vv build --tag', path=path))
        del_tree(path)

    def test_unicorn(self):
        path = os.path.join(self.wdir, self.name)
        del_tree(path)
        inputs = self.name, self.doc, self.author, self.email, self.url
        file_path = os.path.join(self.wdir, self.name + '_details')
        with open(file_path, "w") as f:
            f.write(os.linesep.join(inputs))
        self.assertEqual(0, auxilium('-vv create < %s' % file_path,
                                     path=self.wdir))

        self.assertEqual(0, auxilium('-vv update', path=path))
        self.assertEqual(0, auxilium('-vv test', path=path))
        self.assertEqual(0, auxilium('-vv doc --api', path=path))
        self.assertEqual(0, auxilium('-vv build', path=path))
        del_tree(path)


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
