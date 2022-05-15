import json
import os
import requests

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)

def url_currency(currency) :
  url_currency = 'http://www.floatrates.com/daily/' + currency + '.json'
  return url_currency

def save_data(url,currency) :
    
    data_json = requests.get(url).json()
    path = os.path.join(fileDirectory, currency+'.json')
    with open(path,'w') as file:
        json.dump(data_json,file)

def rate_value(dev1,dev2):
    path = os.path.join(fileDirectory, dev1+'.json')
    with open(path,'r') as file :
        data = json.load(file)
    rate = data[dev2.lower()]['rate']
    return rate


