# -*- coding: utf-8 -*-

# auxilium_demo
# -------------
# a demo by auxilium (created by auxilium)
#
# Author:   auxilium
# Version:  0.1, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__doc__ = 'a demo by auxilium (created by auxilium)'
__license__ = 'Apache License 2.0'

__author__ = 'auxilium'
__email__ = 'sonntagsgesicht@icould.com'
__url__ = 'https://github.com/sonntagsgesicht/auxilium'

__date__ = 'Wednesday, 29 September 2021'
__version__ = '0.1'
__dev_status__ = '3 - Alpha'

__dependencies__ = ()
__dependency_links__ = ()
__data__ = ()
__scripts__ = ()

# this is just an example to demonstrate the auxilium workflow
# it can be removed safely


class Line(object):
    r""" This a example class (by auxilium)

    The |Line| objects implements a straight line,
    i.e. a function $y = f(x)$ with

    .. math::

        f(x) = a + b \cdot x

    where $a$ and $b$ are numbers.

    >>> from auxilium_demo import Line
    >>> a, b = 1, 2
    >>> line = Line(a, b)
    >>> line.y(x=3)
    7
    >>> line(3)  # Line objects are callable
    7
    >>> line.a
    1
    >>> line.b
    2

    """
    def __init__(self, a=0, b=1):
        self._a = a
        self._b = b

    @property
    def a(self):
        """ a value """
        return self._a

    @property
    def b(self):
        """ b value """
        return self._b

    def y(self, x=1):
        """ gives y value depending on x value argument

        :param x: x value
        :return: $a + b * x$

        """
        return self._a + self._b * x

    def __call__(self, x=1):
        return self.y(x)
