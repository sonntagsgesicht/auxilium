#!/usr/bin/env python3

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Tuesday, 28 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from .root import add_arguments as root  # noqa: F401
from .create import add_arguments as create  # noqa: F401
from .update import add_arguments as update  # noqa: F401
from .test import add_arguments as test  # noqa: F401
from .doc import add_arguments as doc  # noqa: F401
from .deploy import add_arguments as deploy  # noqa: F401
from .python import add_arguments as python  # noqa: F401

from .formatter import ArgumentDefaultsAndConstsHelpFormatter  # noqa: F401
