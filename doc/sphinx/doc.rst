
-----------------
CLI Documentation
-----------------

.. toctree::
    :glob:


main commands and options
-------------------------


.. doctest::

    import os; os.system("auxilium -h")


.. code-block:: console

    $ auxilium -h
    usage: auxilium [-h] [-v] [-V] [-e [PATH]] [-x] [-p [SCRIPT]] [-d [NAME]]
                    {create,update,test,doc,build,python} ...

        creates and manages boilerplate python development workflow.
         [ create > exit_status > test > build > deploy ]


    positional arguments:
      {create,update,test,doc,build,python}
        create              creates a new project, repo and virtual environment
        update              keeps project, repo and dependencies up-to-date
        test                checks project integrity by testing using `unittest`
                            framework
        doc                 builds project documentation using `sphinx`
        build               builds project distribution and deploy releases to
                            `pypi.org`
        python              invokes python in virtual environment

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbosity       set logging level (-v=ALL, -vv=DEBUG, -vvv=INFO,
                            -vvvv=WARNING, -vvvvv=ERROR) (default: INFO) (default:
                            0)
      -V, --version         show version and exit (default: False)
      -e [PATH], --env [PATH]
                            set path to python executable or virtual environment.
                            to use system interpreter just set empty flag `-e`
                            (default: .aux/venv/bin/python3.9)
      -x, --exit-status     exit status in case of failure (-x for zero, -xx for
                            non-zero, -xxx for raise exception) (default: non-zero
                            (default: 0)
      -p [SCRIPT], --pre [SCRIPT]
                            pre run script, which is executed before every command
                            (except 'create' and 'python') (default: ./PRE)
      -d [NAME], --demo [NAME]
                            starts a demo in creating a repo (default value if
                            flagged: auxilium_demo)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."


.. .. image:: ../pix/auxilium_cli.jpg

.. code-block:: console

    $ auxilium --version

    auxilium 0.2.1 from /usr/local/lib/python3.9/site-packages/auxilium (python3.9)


create command and its options
------------------------------

.. code-block:: console

    $ auxilium create -h

    usage: auxilium create [-h] [--name NAME] [--slogan SLOGAN] [--author AUTHOR]
                           [--email EMAIL] [--url URL] [--venv [PATH]] [--update]
                           [--commit [MSG]] [--cleanup]

    creates a new project, repo and virtual environment
         with project file structure from templates which has already set-up
         `venv` virtual python environment to run and test projects isolated
         `git` source code repository for tracking source exit_status changes
         `unittest` suite of tests to ensure the project works as intended
          already-to-use documentation structure build for `sphinx`


    optional arguments:
      -h, --help       show this help message and exit
      --name NAME      project name
      --slogan SLOGAN  project slogan
      --author AUTHOR  project author
      --email EMAIL    project email
      --url URL        project url
      --venv [PATH]    PATH to create virtual python environment (default:
                       .aux/venv)
      --update         just (re)install/update virtual environment (skip to create
                       project as well as commit) (default: False)
      --commit [MSG]   commit on successful creation (default: Initial commit)
      --cleanup        uninstall current project via `pip uninstall` and rollback
                       site-packages (ignores other input) (default: False)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."


.. .. image:: ../pix/auxilium_cli_create.jpg

.. code-block:: console

    $ auxilium create

     Please enter project details.

    Enter project name   : unicorn
    Enter project slogan : Always be a unicorn.
    Enter author name    : dreamer
    Enter project email  : unicorn@home
    Enter project url    : https://www.dreamer.home/unicorn

      🪚 created project %s with files

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


update command and its options
------------------------------

.. code-block:: console

    $ auxilium update -h

    usage: auxilium update [-h] [--upgrade [PKG]] [--install] [--requirements]
                           [--header] [--status] [--commit [MSG]]
                           [--pull [BRANCH]] [--remote REMOTE] [--remote_usr USR]
                           [--remote_pwd PWD] [--cleanup]

    keeps project, repo and dependencies up-to-date

    optional arguments:
      -h, --help        show this help message and exit
      --upgrade [PKG]   upgrade python library [PKG] via `pip` (default value if
                        flagged: pip)
      --install         (re)install current project via `pip install -e .`
                        (default: False)
      --requirements    manage requirements (dependencies) in `requirements.txt`
                        and `upgrade_requirements.txt` (default: False)
      --header          update timestamps and file header of modified files
                        (default: True)
      --status          check status of local `git` repo (default: False)
      --commit [MSG]    commit changes to local `git` repo (default: Commit)
      --pull [BRANCH]   pull from remote `git` repo (requires REMOTE) (default
                        value if flagged: master)
      --remote REMOTE   remote `git` repo (default:
                        https://github.com/sonntagsgesicht/auxilium)
      --remote_usr USR  user on remote `git` repo (default: sonntagsgesicht)
      --remote_pwd PWD  password/token on remote `git` repo (default:
                        ****************************************)
      --cleanup         uninstall current project via `pip uninstall` and rollback
                        site-packages (ignores other input) (default: False)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."


.. .. image:: ../pix/auxilium_cli_update.jpg

.. code-block:: console

    $ auxilium update --install --upgrade='regtest' --requirements

      🛠 run header maintenance
      🤷 no changes to commit
      🏅 upgrade `regtest`
      💔 uninstall project via pip uninstall
      🗜 install project via pip install -e
      🧰 setup environment requirements
      ✅ finished in 21.259s


test command and its options
----------------------------

.. code-block:: console

    $ auxilium test -h

    usage: auxilium test [-h] [-ff] [--commit [MSG]] [--coverage [MIN]]
                         [--quality] [--security] [--cleanup]
                         [TESTMATH]

    checks project integrity by testing using `unittest` framework

    positional arguments:
      TESTMATH          path to directory where test are found (default: test)

    optional arguments:
      -h, --help        show this help message and exit
      -ff, --fail-fast  stop on first fail or error (default: False)
      --commit [MSG]    auto commit on successful test run (default value if
                        flagged: Commit tested)
      --coverage [MIN]  check code coverage of tests - fail on total coverage less
                        than MIN (default: 0)
      --quality         evaluate quality of source code (default: True)
      --security        evaluate security of source code (default: True)
      --cleanup         remove temporary files (default: False)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."


.. .. image:: ../pix/auxilium_cli_test.jpg

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



documentation (doc) command and its options
-------------------------------------------

.. code-block:: console

    $ auxilium doc -h
    usage: auxilium doc [-h] [-ff] [--commit [MSG]] [--api] [--doctest]
                        [--coverage] [--pdf] [--show] [--cleanup]

    builds project documentation using `sphinx`

    optional arguments:
      -h, --help        show this help message and exit
      -ff, --fail-fast  stop on first fail or error (default: False)
      --commit [MSG]    auto commit on successful doc build run (incl. doctest)
                        (default value if flagged: Commit doc build)
      --api             add api entries to docs (default: False)
      --doctest         run doctest, testing code examples in docs (default: True)
      --coverage        run doctest, testing code examples in docs (default: True)
      --pdf             build pdf documentation (`sphinx -M latexpdf`) (default:
                        False)
      --show            show html documentation (default: False)
      --cleanup         remove temporary files (default: False)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."


.. .. image:: ../pix/auxilium_cli_doc.jpg

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


build command and its options
-----------------------------

.. code-block:: console

    $ auxilium build -h

    usage: auxilium build [-h] [--header] [--commit [MSG]] [--tag [TAG]]
                          [--push [BRANCH]] [--remote REMOTE] [--remote_usr USR]
                          [--remote_pwd PWD] [--deploy] [--pypi_usr USR]
                          [--pypi_pwd PWD] [--cleanup]

    builds project distribution and deploy releases to `pypi.org`

    optional arguments:
      -h, --help        show this help message and exit
      --header          update timestamps and file header of modified files
                        (default: True)
      --commit [MSG]    auto commit on successful build (default value if flagged:
                        Commit build)
      --tag [TAG]       auto tag on successful build (default value if flagged:
                        v0.2.1)
      --push [BRANCH]   push to given branch of remote `git` repo - requires
                        REMOTE (default value if flagged: master)
      --remote REMOTE   remote `git` repo (default:
                        https://github.com/sonntagsgesicht/auxilium)
      --remote_usr USR  user on remote `git` repo (default: sonntagsgesicht)
      --remote_pwd PWD  password/token on remote `git` repo (default:
                        ****************************************)
      --deploy          release on `pypi.org` - requires USR and PWD (default:
                        False)
      --pypi_usr USR    user on `pypi.org` (default: sonntagsgesicht)
      --pypi_pwd PWD    password/token on `pypi.org` (default: ********)
      --cleanup         remove temporary files (default: False)

        if (default: True) a given flag turns its value to False.
        default behavior may depend on current path and project.
        set default behavior in `~/.aux/config` and `./.aux/config`."



.. .. image:: ../pix/auxilium_cli_build.jpg

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



python command and its options
------------------------------

.. code-block:: console

    # auxilium python -h

    usage: auxilium python [-h] [-c cmd | -m mod | -f file | -] [arg ...]

    invokes python in virtual environment

    optional arguments:
      -h, --help  show this help message and exit
      -c cmd      program passed in as string (terminates option list)
      -m mod      run library module as a script (terminates option list)
      -f file     program read from script file
      -           program read from stdin (default; interactive mode if a tty)
                  (default value if flagged: True)

      arg         arguments passed to program in sys.argv[1:]

    Call python interpreter of virtual environment (Note: only some standard optional arguments are implemented)


.. .. image:: ../pix/auxilium_cli_python.jpg

.. code-block:: console

    $ auxilium python

      🐍 ...

    Python 3.9.6 (default, Jun 29 2021, 05:25:02)
    [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

