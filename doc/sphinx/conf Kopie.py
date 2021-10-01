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

sys.path.append('../..')

if os.getcwd().find('readthedocs') < 0:
    pkg = __import__(os.getcwd().split(os.sep)[-3])
else:
    pkg = __import__(__file__.split(os.sep)[-6])

from auxilium.rst_tools import rst_replace

rst_prolog = rst_replace(pkg)


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
autodoc_default_options = {
    'show-inheritance': 1,
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'inherit_docstrings': True
    # 'inherited-members': False,
    # 'special-members': '__call__',
    # 'exclude-members': '__weakref__',
    # 'autosummary': True,
}

extensions = [
    'karma_sphinx_theme',
    'sphinx_math_dollar',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
]

numpydoc_show_class_members = True
autoclass_content = 'both'

source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = pkg.__name__.capitalize()
copyright = pkg.__author__
author = pkg.__email__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pkg.__version__
# The full version, including alpha/beta/rc tags.
release = pkg.__version__ + ' [' + pkg.__dev_status__ + ']'
# today as date of release
today = pkg.__date__

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A boolean that decides whether module names are prepended
# to all object names.
add_module_names = True


# -- Options for HTML output ----------------------------------------------

# To use different theme, first add it to extensions.
html_theme = 'karma_sphinx_theme'

# Some themes have a logo.
# html_logo = ''


# -- Options for LaTeX output ---------------------------------------------

latex_logo = 'logo.png'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    master_doc,
    pkg.__name__ + '.tex',
    pkg.__name__.capitalize() + ' Documentation',
    pkg.__author__,
    'manual'
), ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

man_pages = [(
    master_doc,
    pkg.__name__,
    pkg.__name__.capitalize() + ' Documentation',
    [pkg.__author__],
    1)
]
