# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Monday, 27 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())


__doc__ = 'Python project for an automated test and deploy toolkit.'
__version__ = '0.1.5'
__dev_status__ = '2 - Beta'
__date__ = 'Monday, 27 September 2021'
__author__ = 'sonntagsgesicht'
__email__ = __author__ + '@icloud.com'
__url__ = 'https://github.com/' + __author__ + '/' + __name__
__license__ = 'Apache License 2.0'
__dependencies__ = 'pip', 'dulwich', 'pytest', 'flake8', 'bandit', \
                   'sphinx', 'sphinx_rtd_theme', 'sphinx_math_dollar', \
                   'twine',
__dependency_links__ = ()
__data__ = ('data/pkg.zip',)
__scripts__ = ('auxilium/scripts/auxilium',)



from .rst_tools import replacements_str, replacements_from_pkg, \
    replacements_from_cls, replacements
