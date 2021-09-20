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


import os
import sys
import unittest
import logging
import datetime

sys.path.append('..')

pkg = __import__(os.getcwd().split(os.sep)[-1])

logging.basicConfig()


class FirstUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_pkg_name(self):
        self.assertEqual(os.getcwd().split(os.sep)[-1], pkg.__name__)


if __name__ == "__main__":
    start_time = datetime.datetime.now()

    print('')
    print('======================================================================')
    print('')
    print(('run %s' % __file__))
    print(('in %s' % os.getcwd()))
    print(('started  at %s' % str(start_time)))
    print('')
    print('----------------------------------------------------------------------')
    print('')

    unittest.main(verbosity=2)

    print('')
    print('======================================================================')
    print('')
    print(('ran %s' % __file__))
    print(('in %s' % os.getcwd()))
    print(('started  at %s' % str(start_time)))
    print(('finished at %s' % str(datetime.datetime.now())))
    print('')
    print('----------------------------------------------------------------------')
    print('')
