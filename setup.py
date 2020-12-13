import os
import sys
pythonloc = os.path.dirname(sys.executable)
os.rename('doreq.py', pythonloc + '\doreq.py')
