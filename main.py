import json
import requests
from DB import DataBase
f = open('cred.json')
data = json.load(f)
f.close()
#print(data)
HEADERS = data['HEADERS']
resp =requests.get('https://oauth.reddit.com/api/v1/me', headers=HEADERS)
data_base = DataBase()
if resp.status_code == 401:
    print('Getting new headers')
    from auth import get_header    
    HEADERS = get_header()
resp =requests.get('https://oauth.reddit.com/api/v1/me', headers=HEADERS)
parmas = {'limit':10}

subs = data_base.get_subs()
for sub in subs:
    req_link = f'https://oauth.reddit.com/r/{sub}'
    print(req_link,HEADERS)
    res = requests.get(req_link,headers=HEADERS,params = parmas)
    print(sub,res)
    for post in res.json()['data']['children']:
        data_base.add_post(post,sub)
