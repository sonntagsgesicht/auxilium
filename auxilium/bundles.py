
from .tools.setup_tools import setup, create_project
from .tools.test_tools import run, analysis, coverage, profile
from .tools.documentation_tools import sphinx
from .tools.deployment_tools import build, set_timestamp, replace_headers, release, pypideploy

PROFILE_FILE = "dev.py"
TEST_DIR = "test"


def create():
    print('*** create new project ***')
    create_project()
    print('')


def simple(test_dir=TEST_DIR):
    print("*** run simple test pipeline ***")
    setup()
    run(test_dir)
    print('')
    print("*** run simple test pipeline finished ***")


def full(pkg_name, test_dir=TEST_DIR, profile_file=PROFILE_FILE):
    print("*** run full test pipeline ***")
    setup()
    sphinx()
    profile(profile_file)
    analysis(pkg_name)
    coverage(pkg_name, test_dir)
    # codecoverage(CODECOV_TOKEN)
    build()
    print('')
    print("*** run full test pipeline finished ***")


def deploy(pkg_name, github=None, pypi=None):
    print("*** run deployment pipeline ***")
    set_timestamp(pkg_name)
    replace_headers(pkg_name)
    build()
    if github:
        github_usr, github_pwd = github
        release(pkg_name, github_usr, github_pwd)
    if pypi:
        pypi_usr, pypi_pwd = pypi
        pypideploy(pypi_usr, pypi_pwd)
    print('')
    print("*** deployment pipeline finished ***")
