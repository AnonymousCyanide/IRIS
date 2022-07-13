import mysql.connector
import json
from RedCom import Reddit


class DB():
    def __int__():
        data = None
        with open('cred.json') as f:
            data = json.load(f)
        host = data['SqlCred']['host']
        user = data['SqlCred']['user']
        pwd = data['SqlCred']['pwd']
        try :
            self.mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = pwd
            )
            self.cursor = self.mydb.cursor()
            self.cursor.execute('USE iris')
        except :
            self.__del__()
    def __del__(self):
        print('Object Destroyed')
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
            

    def get_subs():
        cursor.execute('SELECT * FROM subreddits')
        subreddits = []
        for x in cursor:
            #print(x)
            subreddits.append(x[0])
        return subreddits


