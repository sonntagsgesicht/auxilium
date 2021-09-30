
.. image:: ../pix/logo.png

Python library *auxilium*
-------------------------

|codeship|_ |readthedocs|_ |license|_ |github_version|_ |pip_version|_
|py_version|_ |pypi_frequency|_ |pypi_downloads|_

.. |codeship| image:: https://img.shields.io/codeship/5b8cc2e0-ac1d-0137-31a2-06d5e6117547/master.svg
.. _codeship: https://codeship.com//projects/362165

.. |readthedocs| image:: https://img.shields.io/readthedocs/auxilium
.. _readthedocs: https://auxilium.readthedocs.io/en/latest/intro.html

.. |license| image:: https://img.shields.io/github/license/sonntagsgesicht/auxilium
.. _license: https://github.com/sonntagsgesicht/auxilium/raw/master/LICENSE

.. |github_version| image:: https://img.shields.io/github/release/sonntagsgesicht/auxilium?label=github
.. _github_version: https://github.com/sonntagsgesicht/auxilium/releases

.. |pip_version| image:: https://img.shields.io/pypi/v/auxilium
.. _pip_version: https://pypi.org/project/auxilium/

.. |py_version| image:: https://img.shields.io/pypi/pyversions/auxilium
.. _py_version: https://pypi.org/project/auxilium/

.. |pypi_frequency| image:: https://img.shields.io/pypi/dm/auxilium
.. _pypi_frequency: https://pypi.org/project/auxilium/

.. |pypi_downloads| image:: https://pepy.tech/badge/auxilium
.. _pypi_downloads: https://pypi.org/project/auxilium/

.. badge issues with twine om windows

.. image https://img.shields.io/codeship/5b8cc2e0-ac1d-0137-31a2-06d5e6117547/master.svg
   :target: https://codeship.com//projects/362165
   :alt: Codeship

.. image https://travis-ci.org/sonntagsgesicht/auxilium.svg?branch=master
   :target: https://travis-ci.org/sonntagsgesicht/auxilium
   :alt: Travis ci

.. image https://img.shields.io/readthedocs/auxilium
   :target: http://auxilium.readthedocs.io
   :alt: Read the Docs

.. image https://img.shields.io/codefactor/grade/github/sonntagsgesicht/auxilium/master
   :target: https://www.codefactor.io/repository/github/sonntagsgesicht/auxilium
   :alt: CodeFactor Grade

.. image https://img.shields.io/codeclimate/maintainability/sonntagsgesicht/auxilium
   :target: https://codeclimate.com/github/sonntagsgesicht/auxilium/maintainability
   :alt: Code Climate maintainability

.. image https://img.shields.io/codecov/c/github/sonntagsgesicht/auxilium
   :target: https://codecov.io/gh/sonntagsgesicht/auxilium
   :alt: Codecov

.. image https://img.shields.io/lgtm/grade/python/g/sonntagsgesicht/auxilium.svg
   :target: https://lgtm.com/projects/g/sonntagsgesicht/auxilium/context:python/
   :alt: lgtm grade

.. image https://img.shields.io/lgtm/alerts/g/sonntagsgesicht/auxilium.svg
   :target: https://lgtm.com/projects/g/sonntagsgesicht/auxilium/alerts/
   :alt: total lgtm alerts

.. image https://img.shields.io/github/license/sonntagsgesicht/auxilium
   :target: https://github.com/sonntagsgesicht/auxilium/raw/master/LICENSE
   :alt: GitHub

.. image https://img.shields.io/github/release/sonntagsgesicht/auxilium?label=github
   :target: https://github.com/sonntagsgesicht/auxilium/releases
   :alt: GitHub release

.. image https://img.shields.io/pypi/v/auxilium
   :target: https://pypi.org/project/auxilium/
   :alt: PyPI Version

.. image https://img.shields.io/pypi/pyversions/auxilium
   :target: https://pypi.org/project/auxilium/
   :alt: PyPI - Python Version

.. image https://img.shields.io/pypi/dm/auxilium
   :target: https://pypi.org/project/auxilium/
   :alt: PyPI Downloads

.. image https://pepy.tech/badge/auxilium
   :target: https://pypi.org/project/auxilium/
   :alt: PyPI Downloads

A Python project for an automated test and deploy toolkit - 100% reusable.


Code, Documentation and Tests
-----------------------------

Modern software development comes as a triple of

.. image:: ../pix/code-test-doc.png

.. :alt: **code is for machines** // **tests links docs and code** // **docs are for humans**

   * The **code** is the actual software program or library which can executed or invoked.

   * The **documentation** should give an introducing the idea and mission, guide how to use it, describe functionality and features.

   * Finally, intensive **tests** increases the confidence that the documented functionality is correctly implemented.


To support this **auxilium** is designed to build, to auto-doc, to test and to deploy
small to medium size Python projects in **3 simple steps**.

   1. copy your **source code** into a boilerplate project structure

   2. write useful **documentation** in your python source code doc strings

   3. add as many as possible **test cases** in a designated test directory structure

Once setup up, **auxilium** provides - out of the box - tools
to build a ci/cd (continuous integration/continuous deployment) framework with

   * conventions on how the project is structured, i.e. where to find source, test and doc files

   * provides useful template structure of files which can be easy modified and extended

   * keeps always a single source of truth for project information (like version number)

   * sets up a clear and straight structure of the project as well as the corresponding documentation

   * minimises the places to edit, e.g. for the documentation there are by default only thre files to edit

   * comes with a shell script to trigger plenty test and analysis routines incl. drafting releases on github.com and distribute on pypi.org

   * uses standard community tools like *unittest*, *pylint*, *coverage*, *sphinx* and more

   * no detailed configurations of any tools are needed, so you can focus completely on coding your project

   * demo of how to use the framework and various services to build true *ci/cd*; a full automated test and deploy pineline.

Moreover, we recommend to use *pyenv* and *virtualenv* to test different python installations, too.


Quick Start a Project
---------------------

Once installed simply invoke :code:`auxilium create` and enter a few project details.

The whole project structure will be created. Full functioning incl. documentation generation, testing, etc..


.. code-block:: bash

    $ auxilium create

    *** create new project ***
    Please enter project details.

    Enter project name  : unicorn
    Enter project slogan: Always be a unicorn.
    Enter author name   : dreamer
    Enter author email  : dreamer@home
    Enter project url   : www.dreamer.home/unicorn

    Created project unicorn with these files:

      unicorn/CHANGES.rst
      unicorn/HOWTO.rst
      unicorn/LICENSE
      unicorn/MANIFEST.in
      unicorn/README.rst
      unicorn/requirements.txt
      unicorn/setup.py
      unicorn/upgrade_requirements.txt

      unicorn/doc/sphinx/conf.py
      unicorn/doc/sphinx/doc.rst
      unicorn/doc/sphinx/index.rst
      unicorn/doc/sphinx/intro.rst
      unicorn/doc/sphinx/logo.png
      unicorn/doc/sphinx/releases.rst
      unicorn/doc/sphinx/tutorial.rst

      unicorn/test/__init__.py
      unicorn/test/unittests.py

      unicorn/unicorn/__init__.py




Default Structure of a Project
------------------------------

The top level of the directory structure consists of three sub-dirs for source, doc and test files
and some more or less standard project files. Assume the project is called *unicorn*.

.. code-block:: bash

   /unicorn (project root dir)

      /.aux/venv (virtual python environment)

      /unicorn (python source files)
      /doc/sphinx (sphinx files)
      /test/unittests (unittest files)

      LICENSE (license to use)

      CHANGES.rst (change history)
      HOWTO.rst (user guide)
      README.rst (introduction)

      requirements.txt (pip dependencies)
      upgrade_requirements.txt (pip dependencies which always have to be upgraded)

      setup.py (configuration file to build a distribution)
      MANIFEST.in (configuration file to build a distribution)

      .gitignore (configuration file - files and folder which git should ignore)

Your python source files can be structured as you like.
Only few information on your project is required
and has to be found in

.. code-block:: bash

   /unicorn/unicorn/__init__.py

Most of them are needed to setup the *pip* installation (using *setuptools*)
as well as the sphinx configuration for generation a documentation.
See here how :code:`unicorn/unicorn/__init__.py` looks like.

.. code-block:: python

   # -*- coding: utf-8 -*-

   # unicorn
   # -------
   # Always be a unicorn.
   #
   # Author:   dreamer
   # Version:  0.1, copyright Thursday, 29 August 2019
   # Website:  https://github.com/dreamer/unicorn
   # License:  Apache License 2.0 (see LICENSE file)


   import logging

   logging.getLogger(__name__).addHandler(logging.NullHandler())

   __doc__ = 'Always be a unicorn.'
   __license__ = 'Apache License 2.0'

   __author__ = 'dreamer'
   __email__ = 'unicorn@home'
   __url__ = 'https://www.dreamer.home/unicorn'

   __date__ = 'Thursday, 29 August 2019'
   __version__ = '0.1'
   __dev_status__ = '3 - Alpha'

   __dependencies__ = ()
   __dependency_links__ = ()
   __data__ = ()
   __scripts__ = ()


On top level we have the following files

.. code-block:: bash

   /auxilium (project root dir)

      LICENSE

      CHANGES.rst
      HOWTO.rst
      README.rst

      requirements.txt
      upgrade_requirements.txt

      setup.py
      MANIFEST.in

      .gitignore

Which serve for

   * **LICENSE** is the license how to use, change or distribute the project.

   * **CHANGES.rst** will contain the whole change and release history

   * **HOWTO.rst** gives a intro how to use your project. This will show up in your documentation as tutorial.

   * **README.rst** is this page which show up on repository homepage at first. Moreover, this will show up in your documentation as introduction.

   * **requirements.txt** are additional python packages, which are required for development and/or testing

   * **upgrade_requirements.txt** are additional python packages (same as *requirements.txt*), which have to be upgraded, i.e. installed by :code:`pip` with the *--upgrade* option. Usually used for dev repos.

   * **setup.py** configs the installation procedure with pip and the meta keywords of your project on pypi.org. Most of the entries are found in the project **__init__.py** file.

   * **MANIFEST.in** configs the files which will be part of the final distribution.

   * **.gitignore** configs git which files and folder to ignore

The folder structure will look like

.. code-block:: bash

   /unicorn (project root dir)

      /.aux/venv (virtual python environment)

      /unicorn (python source files)
      /doc/sphinx (sphinx files)
      /test/unittests (unittest files)

Note that project root dir and python source dir must have the same name.
:code:`.aux/` might contain further files used by *auxilium* like
:code:`.aux/config`.


Automated Documentation Generation
----------------------------------

The documentation is generated by `sphinx <https://www.sphinx-doc.org>`_
and is located at

.. code-block:: bash

   /auxilium (project root dir)

      /doc/sphinx (sphinx files)

**auxilium** extracts all docs from the source code file and links to some top level *rst* files.
So usually no file under :code:`/doc/sphinx` requires to be edited.

The site-map of a documentation will look like this

.. code-block:: bash

   /index.rst
      /intro.rst     -> README.rst
      /tutorial.rst  -> HOWTO.rst
      /doc.rst       -> api/* (generated by *sphinx-apidoc* via :code:`auxilium api`)
      /releases.rst  -> CHANGES.rst

Sphinx has a configuration (*conf.py*) to build *html* and *latex* resp. *pdf* documentation.
The later requires a latex installation to work.

And it can run *code-blocks* of code examples of your documentation.
(But avoid :code:`.. doctest::` *rst*-directive and :code:`|something|` links in README.rst.
This would fail with `setuptools` to serve as `long_description` for `pypi.org <https://pypi.org>`_.

Since only **doc.rst** will not refer to a top level doc file of the project it is generated from the source code.
So here the work starts to write good python doc strings.

But if a more *sphinx* specific file reps. documentation is preferred.
May be in order to provide detailed insights into the project:
Simply delete :code:`api/*` (if existing) and replace the contents of **doc.rst**.


Automated Test and Test Coverage Framework
------------------------------------------

Test are invoked by
`unittest discovery <https://docs.python.org/3/library/unittest.html#test-discovery>`_
which searches by default for files
containing :code:`unittest.TestCase` classes and process them.

Same for measuring the test coverage
using `coverage <https://github.com/nedbat/coveragepy>`_
source code security and quality
using `bandit <https://github.com/PyCQA/bandit>`_
and `flake8 <https://gitlab.com/pycqa/flake8>`_.


.. code-block:: bash

   /auxilium (project root dir)

      /test/unittests (unittest files)



Installation
------------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install auxilium



Development Version
-------------------

The latest development version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade git+https://github.com/sonntagsgesicht/auxilium.git


Contributions
-------------

.. _issues: https://github.com/sonntagsgesicht/auxilium/issues
.. __: https://github.com/sonntagsgesicht/auxilium/pulls

Issues_ and `Pull Requests`__ are always welcome.


License
-------

.. __: https://github.com/sonntagsgesicht/auxilium/raw/master/LICENSE

Code and documentation are available according to the Apache Software License (see LICENSE__).


