import json
import os
from turtle import pos
import requests

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)

def url_currency(currency) :
  url_currency = 'http://www.floatrates.com/daily/' + currency + '.json'
  return url_currency

def del_data(currency):
    path = os.path.join(fileDirectory, currency+'.json')
    os.remove(path)

def saved_back_currency(currency_list):
    path = os.path.join(fileDirectory, 'back_up_currency.json')
    with open(path,'w') as back_up:
        json.dump(currency_list,back_up)

def back_up_currency():
    path = os.path.join(fileDirectory, 'back_up_currency.json')
    with open(path,'a+') as file :
        if os.stat(path).st_size != 0:
            file.seek(0)
            data = json.load(file)
            return data
        else : return []
def save_data(url,currency) :
    
    data_json = requests.get(url)
    if data_json.status_code == 200 :
        data_json = data_json.json()
        path = os.path.join(fileDirectory, currency+'.json')
        with open(path,'w') as file:
            json.dump(data_json,file)
        return 'ok'
    
    else : return data_json.status_code

def rate_value(dev1,dev2):
    path = os.path.join(fileDirectory, dev1+'.json')
    with open(path,'r') as file :
        data = json.load(file)
    rate = data[dev2.lower()]['rate']
    return rate


