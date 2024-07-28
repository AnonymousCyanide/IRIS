import json
import requests
def get_header():
    f = open('cred.json')
    data = json.load(f)
    username = data['username']
    pwd = data['pwd']
    client = data['client-id']
    token = data['token']
    bot = data['Bot']

    # Get authentication object
    auth = requests.auth.HTTPBasicAuth(str(client),str(token))

    payload = {
        'grant_type' :'password',
        'username' : str(username),
        'password' : str(pwd)
    }

    headers = {'User-agent': str(bot)}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=payload, headers=headers)
    # Getting current acces token
    print(res.json())
    TOKEN = res.json()['access_token']
    HEADERS = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    f.close()
    data['HEADERS'] = HEADERS
    with open('cred.json','w') as f:
        json.dump(data,f)
    return HEADERS