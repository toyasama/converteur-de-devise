
import requests

def url_currency(currency) :
  url_currency = 'http://www.floatrates.com/daily/' + currency + '.json'
  return url_currency

def save_data(url,currency,dict_rate="none") :
    data = requests.get(url).json()
    if dict_rate == "none" :
        if currency != 'USD' and currency != 'EUR' :
            dict_rate = {
                'EUR' : data ['eur']['rate'],
                'USD' : data ['usd']['rate']
            }
            return dict_rate
        elif currency == 'USD' :
            dict_rate = {
                'EUR' : data ['eur']['rate'],
            }
            return dict_rate
        elif currency == 'EUR' :
            dict_rate = {
                'USD' : data ['usd']['rate']
            }
            return dict_rate
    else :
        if currency != '' :
            dict_rate [currency] = data[currency.lower()]['rate']
            return dict_rate

def rate_value(currency,dict_rate,url):
    print('Checking the cache...')
    state = False
    for key,value in dict_rate.items() :
        if key == currency : state = True
    
    if not state :
        print("Sorry, but it is not in the cache!")
        dict_rate = save_data(url,currency,dict_rate)
        return dict_rate[currency]
    
    else :
        print('Oh! It is in the cache!')
        return dict_rate[currency]

# if __name__ == "__main__":
#     my_currency = input().upper()
#     my_url_currency = url_currency(my_currency)
#     rate_dict = save_data(my_url_currency,my_currency)
#     exchange_currency = input().upper()
#     money_to_exchange = int(input())
#     rate = rate_value(exchange_currency,rate_dict,my_url_currency)
#     print('You received',round(money_to_exchange * rate,2),exchange_currency)

#     while exchange_currency != '':
#         exchange_currency = input().upper()
#         if exchange_currency != '':
#             money_to_exchange = int(input())
#             rate = rate_value(exchange_currency,rate_dict,my_url_currency)
#             print('You received',round(money_to_exchange * rate,2),exchange_currency)
