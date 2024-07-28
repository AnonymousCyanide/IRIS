import json
import requests

f = open('cred.json')
data = json.load(f)
f.close()
#print(data)
HEADERS = data['HEADERS']
resp =requests.get('https://oauth.reddit.com/api/v1/me', headers=HEADERS)

if resp.status_code == 403:
    print('Getting new headers')
    from auth import get_header    
    HEADERS = get_header()


class Reddit:
    def get_sub_count(sub):
        params = {'limit':2}
        req_link = f'https://oauth.reddit.com/r/{sub}'
        res = requests.get(req_link,headers = HEADERS,params = params)
        try :
            sub_count = res.json()['data']['children'][0]['data']['subreddit_subscribers']
        except :
            return None
        return sub_count
if __name__ == '__main__':
    a = Reddit.get_sub_count('Python')
    print(a)

