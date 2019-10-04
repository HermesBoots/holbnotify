#!/usr/bin/env python3

import holbnotify.all_checker.project_checker as pc
import http.client
import sys
import holbnotify as holn
import holbnotify.sendEmail
import json

proj_url = sys.argv[1]
creds = holn.Creds(*sys.argv[2:])

conn = http.client.HTTPSConnection('intranet.hbtn.io')
body = creds._asdict()
body['scope'] = 'checker'
body = json.dumps(body)
headers = {'Content-Type': 'application/json'}
conn.request('POST', '/users/auth_token.json', body=body, headers=headers)
auth = json.loads(conn.getresponse().read().decode('UTF-8'))
auth_token = auth['auth_token']

proj_url = proj_url + '.json?' + 'auth_token=' + auth_token

conn.request('GET', proj_url)
proj = json.loads(conn.getresponse().read().decode('UTF-8'))

if any(task['checker_available'] for task in proj['tasks']):
    failed_tasks = sorted(pc.LOTC(proj['id'], *creds))
    holbnotify.sendEmail.sendEmail(creds, failed_tasks)
else:
    sys.exit()
