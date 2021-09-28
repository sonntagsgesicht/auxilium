# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from argparse import ArgumentDefaultsHelpFormatter, \
    SUPPRESS, OPTIONAL, ZERO_OR_MORE


class ArgumentDefaultsAndConstsHelpFormatter(ArgumentDefaultsHelpFormatter):

    def _get_help_string(self, action):
        action_help = action.help
        defaulting_nargs = [OPTIONAL, ZERO_OR_MORE]
        if action.default is not None and action.default is not SUPPRESS:
            if '%(default)' not in action.help:
                if action.option_strings or action.nargs in defaulting_nargs:
                    if 'pwd' in action.dest:
                        ast = '*' * len(action.default)
                        action_help += ' (default: %s)' % ast
                    else:
                        action_help += ' (default: %(default)s)'
        elif action.const is not None and action.const is not SUPPRESS:
            if '%(const)' not in action.help:
                action_help += ' (default value if flagged: %(const)s)'
        return action_help
