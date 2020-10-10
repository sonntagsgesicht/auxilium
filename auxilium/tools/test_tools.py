
from os import system, chdir, getcwd


def run(TEST_DIR):
    # 2. running actual test scripts
    print('*** run test scripts ***')
    home = getcwd()
    chdir(TEST_DIR)
    # python3 -m unittest discover -v -s ${TEST_DIR} -p "*.py"
    system('python3 -m unittest discover -v -p "*.py"')
    chdir(home)
    print('')


def test(TEST_DIR):
    run(TEST_DIR)


def profile(PROFILE_FILE):
    print('*** run test profiling ***')
    system("python3 -m cProfile -s tottime %s" % PROFILE_FILE)
    # python3 -m cProfile -o .cprofile ${PROFILE_FILE}
    # python3 -m pstats .cprofile stat
    # snakeviz .cprofile
    print('')


def analysis(NAME):
    print('*** run code analysis scripts ***')
    print('*** run pylint ***')
    system("pylint --exit-zero %s" % NAME)
    # print('*** run flake8 ***')
    # flake8 --exit-zero "${NAME}";
    # print('*** run pycodestyle (aka pep8) ***')
    # pycodestyle "${NAME}";
    print('*** run bandit ***')
    system('bandit -r %s' % NAME)
    print('')


def coverage(NAME, TEST_DIR):
    print('*** run coverage scripts ***')
    home = getcwd()
    chdir(TEST_DIR)
    system('python3 -m coverage run --include="*%s*" --omit="*test?.py" --module unittest discover -v -p "*.py"' % NAME)
    system("python3 -m coverage xml")
    system("python3 -m coverage report")
    system("python3 -m coverage html")
    chdir(home)
    print('')


def codecoverage(CODECOV_TOKEN):
    print('*** run coverage scripts for codecov ***')
    system("coverage")
    system("codecov --token=%s" % CODECOV_TOKEN)
    print('')
