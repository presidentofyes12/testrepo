import requests
def getreq(url):
  r = requests.get(url)
  return r.content
