
.. currentmodule:: auxilium


File structure
--------------

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


Doctests
--------


auxilium cli
============

* general workflow (create [code] update test [write] doc build [--deploy])
* general cli
* use of .aux/config

auxilium create
---------------

* auxilium create --update (usage in ci/existing projects)
* use of venv activate/deactivate resp. :code:`auxilium python`
* default location .aux/venv

auxilium update
---------------

* version numbers in __init__.py (docmaintain/header)
* use if .aux/last.json
* commit (use of git)
* tag -> push

auxilium test
-------------

* lint/security check
* use of unittest
* use of regtest
* coverage

auxilium doc
------------

* general rst intro
* use of __theme__
* use of sphinx_math_dollar
* use of sphinx_pytype_substitution
* doctest
* coverage
* html/epub/latex (readthedocs)

auxilium build
--------------

* docmaintain
* build (dist)
* push (branch) + draw release
* deploy (creates or updates pypi.org)
