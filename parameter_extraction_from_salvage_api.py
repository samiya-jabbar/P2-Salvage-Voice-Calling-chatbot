
import requests
import json

url = "http://65fce20f910c.ngrok.io/get_case"
payload = { 
    "projectname" : "test123"
}

print(type(payload))

headers = {
    'Content-Type': 'application/json',
    'x-salvagedata-api-key' : '426ecdf5-31bd-4b75-b529-12ed523cd6db' 
    }

#r = requests.post(url, data=json.dumps(payload), headers=headers)
r = requests.post(url, data=json.dumps(payload), headers=headers)
status = json.loads(r.content)['result']['projectname']
print(type(status))
print(r.content)
#print(r)