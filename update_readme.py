import requests as r
import pprint as p
import sys as s
import ast
import os
from datetime import datetime as dt



# Get Existing List
def read_file(file,content):
    with open(file,'r') as f:
        for line in f:
            content += [[line]]              # content += [line[:-1]]             # also works-1


# Get New List
def get_repos_list(user,file,content,logs):
    new_content = content+[]

    # response = re.get('https://api.github.com/users/cod-lab/repos?sort=created, timeout=10)           # also works
    payload = {'sort': 'created'}
    response = r.get('https://api.github.com/users/' + user + '/repos', params=payload, timeout=20).json()        # got list of user's all public repos

    # getting filtered list (latest 5 public repos which are not forked)
    j=1
    for i in range(len(response)):
        if response[i]['fork'] == False:
            new_content[j+40] = ["* [" + response[i]['name'] + "](" + response[i]['html_url'] + ")\n"]
            j+=1
        if j>5: break

    if j<5: 
        logs_fn(logs,"Less than 5 repos in github account")
        s.exit("\nError: less than 5 repos available")          # terminate prgm right away after printing msg

    if content != new_content:
        print('\nwrite_file block----------------------\n')
        write_file(file,new_content)
        print('\nwrite_file block end------------------\n')


# OverWrite New List to file if there's any difference
def write_file(file,content):
    with open(file,'w') as f:
        for i in range(1,len(content)):
            f.write(content[i][0])              # f.write(content[i][0][:-1])             # also works-1


# writing err logs
def logs_fn(logs,e):
    errs={}
    if os.path.exists(logs) and os.stat(logs).st_size != 0:
        errs = ast.literal_eval(open(logs,'r').read())          # ast => str --> dict 

    err={}
    err[len(errs)+1] = {str(dt.now()):e}

    errs.update(err)

    open(logs,'w').write(str(errs).replace("{1: {'" , "{\n\t1: {'").replace("'}, " , "'},\n\t").replace("'}}" , "'}\n}"))



user='cod-lab'
file='README.md'
content=[[]]
logs='Logs'


print('\nread_file block----------------------\n')
try: read_file(file,content)
except FileNotFoundError:
    logs_fn(logs,"FileNotFoundError")
    s.exit('No such file!!\nEnter correct file name..or create one!')          # terminate prgm right away after printing msg
print('\nread_file block end------------------\n')


print('\nget_repos block----------------------\n')
try: get_repos_list(user,file,content,logs)
except r.exceptions.ConnectTimeout:
    logs_fn(logs,"ConnectTimeout")
    s.exit('The server is not responding currently!!\nPlease try again later..')    # problem connecting srvr or srvr not responding   # terminate prgm right away after printing msg
except r.exceptions.ReadTimeout:
    logs_fn(logs,"ReadTimeout")
    s.exit('Unable to read response received from requested api currently!!\nPlease try again later..')   # unable to read received response  # terminate prgm right away after printing msg
except r.exceptions.ConnectionError:
    logs_fn(logs,"ConnectionError")
    s.exit('Your internet is not working currently!!\nPlease try again later..')   # no internet available  # terminate prgm right away after printing msg
print('\nget_repos block end------------------\n')


# print("content: ")
# p.pprint(content, indent=2)#, width=3)
# for i in range(1,len(content)):
#     print(i,content[i][0][:-1])
