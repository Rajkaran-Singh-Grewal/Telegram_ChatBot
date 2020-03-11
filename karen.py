# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:16:14 2019

@author: TomaicazyX
"""


import json as json
import configparser as cfg
import requests
import os
import random
class telegram_chatbot():
    def __init__(self,config):
        self.token= self.read_token_from_config_file(config)
        self.base="https://api.telegram.org/bot{}".format(self.token)
        self.file_id=None
    def get_updates(self, offset=None):
        url=self.base + "/getUpdates?timeout=100"
        if offset:
            url=url+"&offset={}".format(offset + 1)
        r=requests.get(url)
        return json.loads(r.content)
    def send_messages(self,msg,chat_id):
        print(chat_id)
        if msg =="/randomImage2":
            if self.file_id== None:
                url=self.base + "/sendPhoto?chat_id={}".format(chat_id)
                files ={'photo': open('G:/artstation/alberto fernandez/alberto-fernandez-1.jpg','rb')}
                data={"chat_id":"random_image"}
                r=requests.post(url,files=files,data=data)
                print(r.content)
            else:
                url=self.base + "/sendPhoto?chat_id={}".format(chat_id)
                r=requests.post(url,files={'photo':self.file_id})
                print(r.status_code,r.reason,r.content)
                print("sent from server")
        elif msg=="/teenpati":
            requests.get(self.base+"/sendMessage?chat_id={}&text=These are your random cards".format(chat_id))
            a=random.randint(1,52)
            b=random.randint(1,52)
            c=random.randint(1,52)
            file_name="G:/deck/card_{}.png".format(a)
            data={"chat_id":"cards{}".format(a)}
            url=self.base+"/sendPhoto?chat_id={}".format(chat_id)
            r=requests.post(url,files={'photo':open(file_name,'rb')},data=data)
            print(r.content)
            with open('untitled3.json','a+') as f: 
                json.dump(str(r.content),f)
                json.dump("/n/n/n",f)
            file_name="G:/deck/card_{}.png".format(b)
            data={"chat_id":"cards{}".format(b)}
            url=self.base+"/sendPhoto?chat_id={}".format(chat_id)
            r=requests.post(url,files={'photo':open(file_name,'rb')},data=data)
            print(r.content)
            with open('untitled3.json','a+') as f: 
                json.dump(str(r.content),f)
                json.dump("/n/n/n",f)
            file_name="G:/deck/card_{}.png".format(c)
            data={"chat_id":"cards{}".format(c)}
            url=self.base+"/sendPhoto?chat_id={}".format(chat_id)
            r=requests.post(url,files={'photo':open(file_name,'rb')},data=data)
            print(r.content)
            with open('untitled3.json','a+') as f: 
                json.dump(str(r.content),f)
                json.dump("/n/n/n",f)
                    
            
                
        else:
            url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id,msg)
            print(url)
            if msg is not None:
                print(msg)
                requests.get(url)
                print("sent to requests")
    def read_token_from_config_file(self,config):
        parser=cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')
    def showHelp(self,helps,chat_id):
        for i in helps:
            requests.get(self.base + "/sendMessage?chat_id={}&text={}".format(chat_id,i))
        
    def Game(self,b):
        a=random.randint(1,3)
        print(a)
        print(b)
        if (b!=0 ):
               if (a==1):
                    if (b==1):
                        return 1
                    
                    elif b==2:
                        return 2
                    
                    elif b==3:
                        return 3
                    elif a==2:
                        if (b==1):
                            return 3
                        elif b==2:
                            return 1
                        elif b==3:
                            return 2
                    elif a==3:
                          if (b==1):
                              return 3
                          elif b==2:
                              return 2
                          elif b==3:
                              return 1
        