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


import sys
import os
import unittest
import datetime
import shutil

from auxilium.tools.system_tools import module

sys.path.append('..')

CWD, _ = os.path.split(__file__)


def auxilium(command):
    return(module('auxilium', command))


class CreateRepoUnitTests(unittest.TestCase):
    def setUp(self):
        os.chdir(CWD)
        self.wdir = 'working_dir'
        self.name = 'unicorn'
        self.doc = 'Always be a unicorn.'
        self.author = 'dreamer'
        self.email = '<name>@home'
        self.url = 'https://<author>.home/<name>'
        if os.path.exists(self.wdir):
            shutil.rmtree(self.wdir)
        os.mkdir(self.wdir)
        os.chdir(self.wdir)

    def tearDown(self):
        os.chdir('..')
        if os.path.exists(self.wdir):
            shutil.rmtree(self.wdir)
            os.mkdir(self.wdir)

    def test_auxilium_demo(self):
        self.assertEqual(0, auxilium('-z -vv -e="" -demo'))
        self.assertEqual(0, os.system('auxilium -z -vv -demo'))

        os.chdir('auxilium_demo')
        os.chdir('auxilium_demo')
        self.assertEqual(0, auxilium('-z -vv update'))
        self.assertEqual(0, auxilium('-z -vv test'))
        self.assertEqual(0, auxilium('-z -vv doc'))
        self.assertEqual(0, auxilium('-z -vv deploy'))

        self.assertNotEqual(0, auxilium('deploy -z -vv --tag'))

    def test_unicorn(self):
        inputs = self.name, self.doc, self.author, self.email, self.url
        with open('%s_details' % self.name, "w") as f:
            f.write(os.linesep.join(inputs))
        self.assertEqual(0, auxilium('-z -vv create < %s_details' % self.name))

        os.chdir(self.name)
        self.assertEqual(os.getcwd().split(os.sep)[-1], self.name)

        self.assertEqual(0, auxilium('-z -vv update'))
        self.assertEqual(0, auxilium('-z -vv test'))
        self.assertEqual(0, auxilium('-z -vv doc'))
        self.assertEqual(0, auxilium('-z -vv deploy'))


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
