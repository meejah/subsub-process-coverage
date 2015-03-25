import subprocess
import os

"""
Run me with:
py.test test_coverage.py
"""

os.environ['COVERAGE_PROCESS_START'] = '/home/mike/work-tavendo/src/crossbartest/.coveragerc'

def test_coverage():
    # definitely not sub-coverage
    #sub = subprocess.Popen(['python', '-m', 'thing/sub.py'])
    # this gives "sub" coverage
    sub = subprocess.Popen(['coverage', 'run', '--debug', 'dataio', '-p', 'thing/sub.py'])
    sub.wait()
    print "done main"
