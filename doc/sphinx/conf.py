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

# -- Import project pkg ---------------------------------------------------

pos = -5 if 'readthedocs' in __file__ else -3  # hack for readthedocs.org
pkg_path = __file__.split(os.sep)[:pos]
for path in (('..', '..'), pkg_path):
    if path not in sys.path:
        if 'readthedocs' in __file__:
            print('add to sys.path', path)
        sys.path.append(os.sep.join(path))
pkg = __import__(pkg_path[-1])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
]

# Extend extensions by project theme
if pkg.__theme__ and pkg.__theme__.replace('-', '_') not in extensions:
    extensions.append(pkg.__theme__.replace('-', '_'))

autodoc_default_options = {
    'show-inheritance': 1,
    'members': True,  # 'var1, var2',
    'member-order': 'bysource',
    # 'inherited-members': False,
    # 'special-members': '__call__',
    'undoc-members': True,
    # 'exclude-members': '__weakref__',
    # 'autosummary': True,
    'inherit_docstrings': True
}
numpydoc_show_class_members = True
autoclass_content = 'both'
# autosummary_generate = True

# needed for version 1.8.5 (python 2.7)
autodoc_default_flags = ['members', 'show-inheritance']
autodoc_member_order = 'bysource'  # 'groupwise'
autodoc_inherit_docstrings = True

# source_suffix = ['.rst', '.md']
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

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `to_do` and `to_do_List` produce output, else they produce nothing.
todo_include_todos = False

# A boolean that decides whether module names are prepended to all object names.
add_module_names = True

# -- Options for HTML output ----------------------------------------------

if pkg.__theme__:
    html_theme = pkg.__theme__.replace('-', '_')

# html_logo = 'logo.png'
# html_theme_options = {}
# html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_logo = '../pix/logo.png'
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
