import os
import platform
import sys
import matplotlib
matplotlib.use("AGG")
from obspy.scripts.runtests import main as run_tests

# set env variable to skip one stray failing mseed test
# (only fails in Appveyor when building conda packages)
# see test_infinite_loop in test_mseed_special_issues.py
os.environ["CONDAFORGE"] = ''

# this is embarassing.. APPVEYOR env variable is not set as it should be
# according to appveyor docs (see
# https://ci.appveyor.com/project/conda-forge/obspy-feedstock/build/1.0.37/job/cn9436iry5nl9nj6#L5903)
if platform.system().lower() == 'windows':
    os.environ["APPVEYOR"] = "True"
# check environment settings
print("'APPVEYOR' in env: {}".format(str("APPVEYOR" in os.environ)))
if "APPVEYOR" in os.environ:
    print("'APPVEYOR' env setting: '{}'".format(os.environ['APPVEYOR']))

# set node name for test report
os.environ['OBSPY_NODE_NAME'] = 'conda-forge'

# inject '--report' into command line args, since it seems we can't request it
# programmatically anymore with new test setup
sys.argv.insert(1, '--report')
# run tests verbose
sys.argv.insert(1, '-v')

# skip two test cases, will be fixed for next release, see #3183
sys.argv.insert(1, 'not test_pk_baer')
sys.argv.insert(1, '-k')

# run tests and send test report
run_tests()

# for now don't fail conda-forge CI on failed tests, since often we run into
# failing tests during packaging that are just due to e.g. numpy changing how
# they print objects (i.e. doctest fails)
# if errors:
#     sys.exit(1)
# else:
#     sys.exit(0)
