import requests, json
case_ID = 100
data = {"case_id":case_ID}

url = 'https://12498d0ca70c.ngrok.io/get_case'


headers = {
    'Content-Type': 'application/json'
    }

res = requests.post(url, data=json.dumps(data), headers=headers)

project_status = json.loads(res.content)['result']['project_status']
project_type = json.loads(res.content)['result']['project_type']
print(project_status)
print(project_type)

