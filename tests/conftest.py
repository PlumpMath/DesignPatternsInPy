# Content of conftest.py
import sys

collect_ignore = []

# collect_ignore['setup.py'] ## This is typically ignored during tests

if sys.version_info[0] > 2:
    ## Py3 behavior
    ## py.test --collect-only
    collect_ignore.append('singleton_py2_test.py')
else:
    ## Py2 behavior
    ## py.test2 --collect-only
    collect_ignore.append('singleton_py3_test.py')

