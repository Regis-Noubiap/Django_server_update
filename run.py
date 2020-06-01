#!/usr/bin/env python3 

import os 
import requests
import json

user = os.environ.get('USER')
path = '/home/'+user+'/Django_server_update/feedback' 
server_ip = '34.71.41.24'
comment_f = os.listdir(path)
keys = ['title','name','date','feedback']
dict = {} 
for file in comment_f: 
  if not file.startswith('.'): 
    with open(path+'/'+file,'r') as f: 
      x = 0 
      for line in f:
        if str(x)=='0' and not "".join(line.strip().split()).isalnum():
          raise Exception("Please Enter a Title")
        elif str(x)== '1' and not "".join(line.strip().split()).isalnum():
          line = 'Anonymous'
        if str(x)=='4':
          dict[keys[x]] =+ line
          continue 
        dict[keys[x]] = line
        print(dict)
        x = x + 1
        print(x)  
      response = requests.post("http://"+server_ip+"/feedback/",data = dict)
      print(response.status_code)

#print(dict)
#response.raise_for_status() 

