import mysql.connector
import json
from RedCom import Reddit
def check_ele(l,s):
    for i in l:
        if i in s:
            return True
    return False

class DataBase():
    def __init__(self):
        print('object made')
        data = None
        with open('cred.json') as f:
            data = json.load(f)
            print(data)
        host = data['SqlCred']['host']
        user = data['SqlCred']['user']
        pwd = data['SqlCred']['pwd']
        try :
            self.mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = pwd
            )
            self.cursor = self.mydb.cursor(buffered = True)
            self.cursor.execute('USE iris')
            print('Done')
        except :
            self.__del__()
    def __del__(self):
        print('Object Destroyed')
    # Update susbcriber count in subreddit
    def refresh_subreddit(self):
        self.cursor.execute('SELECT * FROM subreddits')
        subreddits = []
        for x in cursor:
            #print(x)
            subreddits.append(x[0])
        print(subreddits)
        for sub in subreddits:
            count = Reddit.get_sub_count(sub)
            if count == None:
                print(sub,'Key notfound')
                continue
            query = f'UPDATE subreddits SET sub_count = "{count}" WHERE sub_name = "{sub}"'
            #print(query)
            
            self.cursor.execute(query)
            self.mydb.commit()
            
    # gets a list of all subs 
    def get_subs(self):
        self.cursor.execute('SELECT * FROM subreddits')
        subreddits = []
        for x in self.cursor:
            #print(x)
            subreddits.append(x[0])
        return subreddits
    #adds to posts table in data base
    def add_post(self,post,sub):
        id = post['kind'] + '_' + post['data']['id']
        query = f'SELECT * FROM posts WHERE id = "{id}"'
        self.cursor.execute(query)
        if self.cursor.rowcount != 0:
            print('post already here')
            return None
        try :
            content  = post['data']['selftext']
            if len(content) > 200 or check_ele(['"',"'"],content):

                with open(f'content/{id}.txt','w') as f:
                    f.write(content)
                    content = f'content/{id}.txt'


            query = f''' 
            INSERT INTO posts VALUES(
                    "{id}",
                    "{sub}",
                    "{post['data']['title']}",
                    "{content}",
                    "{post['data']['upvote_ratio']}",
                    "{post['data']['score']}"
                                            );
                    '''
            try :
                self.cursor.execute(query)
                self.mydb.commit()
                print('posts added sub :',sub)
            except :
                print('Query error')
                if sub == 'BlankPagesEmptyMugs':
                    print(query)
        except :
            print('error in keys ',sub)

       
         


