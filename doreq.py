import requests
def getreq(url):
  r = requests.get(url)
  return r.content
def tostr(variable):
  return variable.decode("utf-8")
