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
        self.level = ''  # '-vv'
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
        self.assertEqual(0, auxilium('%s -demo' % self.level, path=self.wdir))

        self.assertEqual(0, auxilium('%s update' % self.level, path=path))
        self.assertEqual(0, auxilium('%s test --fail-fast' % self.level,
                                     path=path))
        self.assertEqual(0, auxilium('%s doc --api --fail-fast' % self.level,
                                     path=path))
        self.assertEqual(0, auxilium('%s build' % self.level, path=path))

        self.assertEqual(0, auxilium('%s build --tag' % self.level, path=path))
        self.assertNotEqual(0, auxilium('%s build --tag' % self.level,
                                        path=path))
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
