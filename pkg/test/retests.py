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


from os import getcwd
from os.path import basename
from regtest import RegressionTestCase


pkg = __import__(basename(getcwd()))


class FirstRegTests(RegressionTestCase):
    def setUp(self):
        pass

    def test_sample(self):
        self.assertAlmostRegressiveEqual(1, pkg.Line(0, 1).y(x=1))
