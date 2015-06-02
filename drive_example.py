import json
import webbrowser

import httplib2

from apiclient import discovery
from oauth2client import client


class AuthCache:
  def __init__(self):
    print "initializing"
    #self.data = []
    pass

  def get(self,key,namespace):
    print "%s - %s" % (key,namespace)
    return None

  def set(self,filename, obj, namespace):
    print "%s - %s - %s" % (filename,obj,namespace)
    return None

if __name__ == '__main__':
  
  new_cache = AuthCache()

  flow = client.flow_from_clientsecrets(
    'client_secrets.json',
    scope='https://www.googleapis.com/auth/drive.metadata.readonly',
    redirect_uri='urn:ietf:wg:oauth:2.0:oob',
    code="4/oS-7FwnxwMbf1EXnE5hSYpQ4C5QMxpfgaX-WL_LxpjQ.8k_0PeWxFjUUoiIBeO6P2m_YiexmmwI",
    cache=new_cache)

  auth_uri = flow.step1_get_authorize_url()
  webbrowser.open(auth_uri)

  auth_code = raw_input('Enter the auth code: ')

  credentials = flow.step2_exchange(auth_code)
  http_auth = credentials.authorize(httplib2.Http())
  import pdb ; pdb.set_trace()
  print http_auth

  drive_service = discovery.build('drive', 'v2', http_auth)
  files = drive_service.files().list().execute()
  for f in files['items']:
    print f['title']
