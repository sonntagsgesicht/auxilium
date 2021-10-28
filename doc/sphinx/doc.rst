
-----------------
CLI Documentation
-----------------

.. toctree::
    :glob:


:code:`auxilium` and options
----------------------------


.. command-output:: auxilium -h

.. program-output:: python3 -c 'import auxilium, sys; print("auxilium %s from .../site-packages/auxilium (%s)" % (auxilium.__version__, sys.executable))'


:code:`auxilium create` and options
-----------------------------------

.. command-output:: auxilium create -h

.. code-block:: console

    $ auxilium create

     Please enter project details.

    Enter project name   : unicorn
    Enter project slogan : Always be a unicorn.
    Enter author name    : dreamer
    Enter project email  : unicorn@home
    Enter project url    : https://www.dreamer.home/unicorn

      🪚 created project unicorn with files

           unicorn/.gitignore
           unicorn/CHANGES.rst
           unicorn/HOWTO.rst
           unicorn/LICENSE
           unicorn/MANIFEST.in
           unicorn/README.rst
           unicorn/requirements.txt
           unicorn/setup.py
           unicorn/upgrade_requirements.txt

           unicorn/test/regtests.py
           unicorn/test/unittests.py

           unicorn/.aux/config


           unicorn/doc/sphinx/conf.py
           unicorn/doc/sphinx/doc.rst
           unicorn/doc/sphinx/index.rst
           unicorn/doc/sphinx/intro.rst
           unicorn/doc/sphinx/logo.png
           unicorn/doc/sphinx/releases.rst
           unicorn/doc/sphinx/tutorial.rst

           unicorn/unicorn/__init__.py

      🛠 run header maintenance
      👻 create virtual environment
      🏅 upgrade `pip`
      🗜 install project via pip install -e
      🧰 setup environment requirements
      🐣 init local `git` repo
      ➕ add/stage files to local `git` repo
      📌 commit changes to local `git` repo
      🏁 project setup finished

     Consider a first full run via:

       > cd unicorn
       > auxilium test
       > auxilium doc --api
       > auxilium build
       > auxilium doc --show

      ✅ finished in 90.295s

Now don't forget

.. code-block:: console

    $ cd unicorn


:code:`auxilium update` and options
-----------------------------------

.. command-output:: auxilium update -h



:code:`auxilium test` and options
---------------------------------

.. command-output:: auxilium test -h


.. code-block:: console

    $ auxilium test

      🔍 evaluate quality of source code
      🚨 evaluate security of source code
      ⛑ run test scripts
         | test_sample_almost_equal (regtests.FirstRegTests) ... ok
         | test_sample_equal (regtests.FirstRegTests) ... ok
         | test_pkg_name (unittests.FirstUnitTests) ... ok
         | test_sample (unittests.FirstUnitTests) ... ok
         |
         | ----------------------------------------------------------------------
         | Ran 4 tests in 1.254s
         |
         | OK
      📑 run test coverage scripts
         | Name                  Stmts   Miss  Cover   Missing
         | ---------------------------------------------------
         | unicorn/__init__.py      29      3    90%   68, 73, 85
         | ---------------------------------------------------
         | TOTAL                    29      3    90%
      ✅ finished in 7.790s


:code:`auxilium doc` and options
--------------------------------

.. command-output:: auxilium doc -h

.. code-block:: console

    $ auxilium doc --api

      🧹 clean environment
      📌 run apidoc scripts
      ⛑ run doctest scripts
      📑 run coverage scripts
         | Undocumented Python objects
         | ===========================
         |
      🌐 build html documentation
      🪧 build single-html documentation
      📕 build epub documentation
      📒 build latex documentation
      ✅ finished in 11.544s


:code:`auxilium build` and options
----------------------------------

.. command-output:: auxilium build -h

.. code-block:: console

    $ auxilium build --commit='inital commit' --push --deploy

      🧹 cleanup build
      🛠 run header maintenance
      🏗 build package distribution
      ➕ add/stage files to local `git` repo
      📌 commit changes to local `git` repo
      📤 push to 'master' to remote `git` repo
      🛫 deploy release on `pypi.org`
      ✅ finished in 6.276s



:code:`auxilium python` and options
-----------------------------------

.. command-output:: auxilium python -h

.. code-block:: console

    $ auxilium python

      🐍 running .aux/venv/bin/python3

    Python 3.9.6 (default, Jun 29 2021, 05:25:02)
    [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>



:code:`auxilium` as Python Function
-----------------------------------

:code:`auxilium` works as python function, too.

.. code-block:: python

    >>> from os import chdir
    >>> from auxilium import auxilium
    >>> auxilium("create --name=unicorn "
                 "--slogan='Always be a unicorn' --author=dreamer "
                 "--email=dreamer@home --url='https://<author>.home/<name>'")

    Please enter project details.

    Enter project name   : unicorn
    Enter project slogan : Always be a unicorn
    Enter project author : dreamer
    Enter project email  : dreamer@home
    Enter project url    : https://<author>.home/<name>

    🪚 created project unicorn with files

       unicorn/.gitignore
       unicorn/CHANGES.rst
       unicorn/HOWTO.rst
       unicorn/LICENSE
       unicorn/MANIFEST.in
       unicorn/README.rst
       unicorn/requirements.txt
       unicorn/setup.py
       unicorn/upgrade_requirements.txt

       unicorn/test/regtests.py
       unicorn/test/unittests.py

       unicorn/.aux/config


       unicorn/doc/sphinx/conf.py
       unicorn/doc/sphinx/doc.rst
       unicorn/doc/sphinx/index.rst
       unicorn/doc/sphinx/intro.rst
       unicorn/doc/sphinx/logo.png
       unicorn/doc/sphinx/releases.rst
       unicorn/doc/sphinx/tutorial.rst

       unicorn/unicorn/__init__.py

    🛠 run header maintenance
    👻 create virtual environment
    🏅 upgrade `pip`
    🗜 install project via pip install -e
    🧰 setup environment requirements
    🐣 init local `git` repo
    ➕  add/stage files to local `git` repo
    📌 commit changes to local `git` repo
    🏁 project setup finished

    Consider a first full run via:

    > cd unicorn
    > auxilium test
    > auxilium doc --api
    > auxilium update --commit="added api doc"
    > auxilium build
    > auxilium doc --show

    ✅  finished in 37.981s

    >>> chdir("unicorn")
    >>> auxilium("test")

    🔍 evaluate quality of source code
    🚨 evaluate security of source code
    ⛑  run test scripts
     | test_sample_almost_equal (regtests.FirstRegTests) ... ok
     | test_sample_equal (regtests.FirstRegTests) ... ok
     | test_pkg_name (unittests.FirstUnitTests) ... ok
     | test_sample (unittests.FirstUnitTests) ... ok
     |
     | ----------------------------------------------------------------------
     | Ran 4 tests in 3.808s
     |
     | OK
    📑 run test coverage scripts
     | Name                  Stmts   Miss  Cover   Missing
     | ---------------------------------------------------
     | unicorn/__init__.py      29      3    90%   68, 73, 85
     | ---------------------------------------------------
     | TOTAL                    29      3    90%
    ✅  finished in 22.588s

    >>> auxilium("doc --api")

    🧹 clean environment
    📌 run apidoc scripts
    ⛑  run doctest scripts
    📑 run coverage scripts
     | Undocumented Python objects
     | ===========================
     |
    🌐 build html documentation
    🪧 build single-html documentation
    📕 build epub documentation
    📒 build latex documentation
    ✅  finished in 12.008s

    >>> auxilium("update --commit")

    🛠 run header maintenance
    ➕  add/stage files to local `git` repo
    📌 commit changes to local `git` repo
    ✅  finished in 1.266s

    >>> auxilium("build")

    🧹 cleanup build
    🛠 run header maintenance
    🏗 build package distribution
    ✅  finished in 1.983s
