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

log_format = "•%(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)


def auxilium(command, path=None):
    return module('auxilium', command, path=path)


class CreateRepoUnitTests(unittest.TestCase):
    def setUp(self):
        self.wdir = os.path.join(CWD, 'working_dir')
        self.name = 'unicorn'
        self.doc = 'Always be a unicorn.'
        self.author = 'dreamer'
        self.email = '<name>@home'
        self.url = 'https://<author>.home/<name>'
        del_tree(self.wdir)
        os.mkdir(self.wdir)
        os.chdir(self.wdir)

    def tearDown(self):
        del_tree(self.wdir)

    def test_auxilium_demo(self):
        self.assertEqual(0, auxilium('-z -vv -e="" -demo', path=self.wdir))
        path = os.path.join(self.wdir, DEMO_PATH)
        #self.assertEqual(0, auxilium('-z -vv update', path=path))
        #self.assertEqual(0, auxilium('-z -vv test', path=path))
        #self.assertEqual(0, auxilium('-z -vv doc', path=path))
        #self.assertEqual(0, auxilium('-z -vv deploy', path=path))

        #self.assertNotEqual(0, auxilium('deploy -z -vv --tag', path=path))

    def _test_unicorn(self):
        inputs = self.name, self.doc, self.author, self.email, self.url
        file_path = os.path.join(self.wdir, self.name + '_details')
        with open(file_path, "w") as f:
            f.write(os.linesep.join(inputs))
        self.assertEqual(0, auxilium('-z -vv create < %s' % file_path,
                                     path = self.wdir))

        path = os.path.join(self.wdir, self.name)

        self.assertEqual(0, auxilium('-z -vv update', path=path))
        self.assertEqual(0, auxilium('-z -vv test', path=path))
        self.assertEqual(0, auxilium('-z -vv doc', path=path))
        self.assertEqual(0, auxilium('-z -vv deploy', path=path))


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
