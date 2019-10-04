#!/usr/bin/env python3

import http.client
import sys
import holbnotify as holn
import json

proj_url = sys.argv[1]
creds = holn.Creds(*sys.argv[2:])

conn = http.client.HTTPSConnections('intranet.hbtn.io')
body = creds._asdict()
body['scope'] = 'checker'
body = json.loads(body)
conn.request('POST', '/users/auth_token.json', body=body)
auth = json.loads(conn.getresponse())
auth_token = auth.auth_token

proj_url = proj_url + '.json?' + 'auth_token=' + auth_token

conn.request('GET', proj_url)
proj = json.loads(conn.getresponse())

if proj['tasks']['checker_available']:
    ------run kyles code----
    ---- send emaiil----
else:
    sys.exit()
