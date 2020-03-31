#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:56:43 2019

@author: kailic
"""



from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd



container = [] #global variable so we can use after running def function
##the website that we will scrape currency exchange rates
url = 'https://www.x-rates.com/table/?from=USD&amount=1'

def crawler(self):
    """
    The crawler will scrape from x-rates.com and collect Top 10 exchange rates.
    The rates will be renew on a daily basis.
    """ 

    webpage = uReq(self).read()
    html = soup(webpage, "html.parser")

    for containers in html.find_all("tr", limit = 11):
        container.append(str(containers.text.strip()))


##run crawler function to collect up-to-date exchange rates
crawler(url)


### clean the exchange rates before using calculator class to exchange your currency
rates = [i.split('\n') for i in container]
rates_df = pd.DataFrame(rates, columns=rates[0])
rates_df.set_index('US Dollar', inplace=True)
rates_df = rates_df.drop('US Dollar')
rates_df = rates_df[['1.00 USD','inv. 1.00 USD']].astype('float64')
#rates_df.dtypes
currencies = rates_df.index.values
#rates_df.to_csv('exchange_rates.csv')

class calculator(object):
    
        
    def USDtoEUR(self):
        if 'Euro' in currencies:
            return self * rates_df.at['Euro','1.00 USD']
        else:
            print('currency not found')
    
    
    def EURtoUSD(self):
        if 'Euro' in currencies:
            return self * rates_df.at['Euro','inv. 1.00 USD']
        else:
            print('currency not found!')
            
    def EURtoCNY(self):
        if 'Euro' and 'Chinese Yuan Renminbi' in currencies:
            return self * (rates_df.at['Euro','inv. 1.00 USD'] * rates_df.at['Chinese Yuan Renminbi','1.00 USD'])
        else:
            print('currency not found!')
 

    def USDtoGBP(self):
        if 'British Pound' in currencies:
            return self * rates_df.at['British Pound','1.00 USD']
        else:
            print('currency not found!')
            
            
    def GBPtoUSD(self):
        if 'British Pound' in currencies:
            return self * rates_df.at['British Pound','inv. 1.00 USD']
        else:
            print('currency not found!')

            
    def USDtoINR(self):
        if 'Indian Rupee' in currencies:
            return self * rates_df.at['Indian Rupee','1.00 USD']
        else:
            print('currency not found!')
    
    
    def INRtoUSD(self):
        if 'Indian Rupee' in currencies:
            return self * rates_df.at['Indian Rupee','inv. 1.00 USD']  
        else:
            print('currency not found!')
  

    def USDtoAUD(self):
        if 'Australian Dollar' in currencies:
            return self * rates_df.at['Australian Dollar','1.00 USD']
        else:
            print('currency not found!')
    
    
    def AUDtoUSD(self):
        if 'Australian Dollar' in currencies:
            return self * rates_df.at['Australian Dollar', 'inv. 1.00 USD']
        else:
            print('currency not found!')
    
    
    def USDtoCAD(self):
        if 'Canadian Dollar' in currencies:
            return self * rates_df.at['Canadian Dollar', '1.00 USD']
        else:
            print('currency not found!')
            
    
    def CADtoUSD(self):
        if 'Canadian Dollar' in currencies:
            return self * rates_df.at['Canadian Dollar', 'inv. 1.00 USD']
        else:
            print('currency not found!')
            
            
    
    def USDtoSGD(self):
        if 'Singapore Dollar' in currencies:
            return self * rates_df.at['Singapore Dollar', '1.00 USD']
        else:
            print('currency not found!')
            
            
    
    def SGDtoUSD(self):
        if 'Singapore Dollar' in currencies:       
            return self * rates_df.at['Singapore Dollar', 'inv. 1.00 USD']
        else:
            print('currency not found!')
            
            
    def USDtoCHF(self):
        if 'Swiss Franc' in currencies:
            return self * rates_df.at['Swiss Franc', '1.00 USD']
        else:
            print('currency not found!')
            


    def CHFtoUSD(self):
        if 'Swiss Franc' in currencies:
            return self * rates_df.at['Swiss Franc', 'inv. 1.00 USD']
        
        else:
            print('currency not found!')
            
    
    
    
    def USDtoMYR(self):
        if 'Malaysian Ringgit' in currencies:
            return self * rates_df.at['Malaysian Ringgit', '1.00 USD']
        else:
            print('currency not found!')  
    
    
    
    def MYRtoUSD(self):
        if 'Malaysian Ringgit' in currencies:
            return self * rates_df.at['Malaysian Ringgit', 'inv. 1.00 USD']
        else:
            print('currency not found!')
            
            
            
       
    def USDtoJPY(self):
        if 'Japanese Yen' in currencies:
            return self * rates_df.at['Japanese Yen', '1.00 USD']
        else:
            print('currency not found!')   
            
            
    
    def JPYtoUSD(self):
        if 'Japanese Yen' in currencies:
            return self * rates_df.at['Japanese Yen', 'inv. 1.00 USD']
        else:
            print('currency not found!')
            
    
    
    def USDtoCNY(self):
        if 'Chinese Yuan Renminbi' in currencies:
            return self * rates_df.at['Chinese Yuan Renminbi','1.00 USD']
        else:
            print('currency not found!')
            
            
            
    def CNYtoUSD(self):
        if 'Chinese Yuan Renminbi' in currencies:
            return self * rates_df.at['Chinese Yuan Renminbi', 'inv. 1.00 USD']
        else:
            print('currency not found!')
            
            
            
    def GBPtoCNY(self):
        if 'British Pound' and 'Chinese Yuan Renminbi' in currencies:
            return self * (rates_df.at['British Pound','inv. 1.00 USD'] * rates_df.at['Chinese Yuan Renminbi','1.00 USD'])
        else:
            print('currency not found!')




#exchange 200 EUR to CAD
#print(calculator.EURtoCAD(200))
