
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


README.rst
----------

Avoid :code:`.. doctest::` *rst*-directive and :code:`|something|`
links in README.rst. This would fail with `setuptools` to serve
as `long_description` for `pypi.org <https://pypi.org>`_.


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
