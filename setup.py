import os
import sys
import requests
pythonloc = os.path.dirname(sys.executable)
cont = requests.get('https://raw.githubusercontent.com/presy12/testrepo/main/doreq.py').content
print("Setting up 'doreq'...")
with open('req.py', 'w') as req:
  req.write(cont.decode("utf-8"))
print("Adding to " + pythonloc + "...")
if os.path.isfile(pythonloc + "/doreq.py"):
  print("Library 'doreq' already installed")
else:
  os.rename('req.py', pythonloc + '\doreq.py')
