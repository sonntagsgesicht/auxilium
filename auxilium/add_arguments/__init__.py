#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from .root import add_arguments as root
from .create import add_arguments as create
from .update import add_arguments as update
from .test import add_arguments as test
from .doc import add_arguments as doc
from .deploy import add_arguments as deploy
from .python import add_arguments as python

from .formatter import ArgumentDefaultsAndConstsHelpFormatter
