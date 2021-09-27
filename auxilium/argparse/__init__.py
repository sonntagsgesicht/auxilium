# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from .create import arg_parser as create
from .update import arg_parser as update
from .test import arg_parser as test
from .doc import arg_parser as doc
from .deploy import arg_parser as deploy
from .python import arg_parser as python
