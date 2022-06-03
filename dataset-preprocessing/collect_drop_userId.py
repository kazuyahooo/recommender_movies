import pandas as pd
from datetime import datetime

df_25M = pd.read_csv('netflix_data_25M.csv')
user_list = set(df_25M.userId.tolist())

start = datetime.now()
print('start time',start)
# small_number_userid = []
for userid in user_list:
    num = df_25M.userId.tolist().count(userid)
    print(userid, num)
    if num < 11:
        # small_number_userid.append(userid)
        with open("drop_userid.txt", "a") as myfile:
            myfile.write(str(userid))
            myfile.write(',')
print('Time taken:',datetime.now()-start)