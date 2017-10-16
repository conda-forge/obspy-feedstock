import os
import sys
import matplotlib
matplotlib.use("AGG")
from obspy.core import run_tests
# set env variable to skip one stray failing test
# (only fails in Appveyor when building conda packages)
os.environ["CONDAFORGE"] = ''
# set env variable to skip code formatting checks
os.environ["OBSPY_NO_FLAKE8"] = ''
# check environment settings
print("'CONDAFORGE' in env: {}".format(str("CONDAFORGE" in os.environ)))
print("'APPVEYOR' in env: {}".format(str("APPVEYOR" in os.environ)))
if "APPVEYOR" in os.environ:
    print("'APPVEYOR' env setting: '{}'".format(os.environ['APPVEYOR']))
# run tests and send test report
errors = run_tests(report=True, hostname="conda-forge", verbosity=2)
if errors:
    sys.exit(1)
else:
    sys.exit(0)
