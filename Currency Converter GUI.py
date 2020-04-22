# -*- coding: utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


#web scraping the most current exchange rates
container = [] #global variable so we can use after running def function
url = "https://www.x-rates.com/table/?from=USD&amount=1"

def crawler(self):
    """
    The crawler will scrape from x-rates.com and collect Top 10 exchange rates.
    """ 

    webpage = uReq(self).read()
    html = soup(webpage, "html.parser")

    for containers in html.find_all("tr", limit = 11):
        container.append(str(containers.text.strip()))

##run crawler function to collect up-to-date exchange rates
crawler(url)


### clean the exchange rates before using calculator class to exchange your currency
rates = [i.split('\n') for i in container]
rates_array = np.array(rates)



root = Tk()
root.title("Currency Converter")


#Create a Image Label Widget
#img_file ="filepath"
#my_img = ImageTk.PhotoImage(Image.open(img_file))
#img = Label(image = my_img)
#img.grid(row=0, column=0, columnspan=2)



#create a Time Label Widget
current_time = datetime.now()
date_time = f"Date: {current_time.year}/ {current_time.month}/ {current_time.day}  Time: {current_time.hour} : {current_time.minute} : {current_time.second}"
time = Label(root, text=date_time)
time.grid(row=0, column=0, columnspan=2)


#Create a Entry Label Widget and Output Label Widget
input_var = StringVar()
output = StringVar()
e = Entry(root, textvariable=input_var, borderwidth=5, width=10)
e.grid(row=1, column=0)

outputLabel = Label(root, textvariable=output)
outputLabel.grid(row=2, column=0)

# #currencies includes Euro, 
#                      British Pound, 
#                      Indian Rupee, 
#                      Australian Dollar, 
#                      Canadian Dollar, 
#                      Singapore Dollar, 
#                      Swiss Franc, 
#                      Malaysian Ringgit, 
#                      Japanese Yen, 
#                      Chinese Yuan Renminbi
#                      US Dollar
curr_list = [("USD","US Dollar"), ("EUR", "Euro"), ("GBP", "British Pound"), ("INR", "Indian Rupee"), 
             ("AUD","Australian Dollar"), ("CAD", "Canadian Dollar"), ("SGD", "Singapore Dollar"), ("CHF", "Swiss Franc"),
             ("MYR", "Malaysian Ringgit"), ("JPY", "Japanese Yen"), ("CNY", "Chinese Yuan Renminbi")]
currencies = []
currency = []
for x, y in curr_list:
    currencies.append(x)
    currency.append(y)


#create OptionMenu Widget and set default values
from_curr = StringVar()
from_curr.set(currencies[0])
to_curr = StringVar()
to_curr.set(currencies[0])


drop_from = OptionMenu(root, from_curr, *currencies)
drop_from.grid(row=1, column=1)
drop_to = OptionMenu(root, to_curr, *currencies)
drop_to.grid(row=2, column=1)

def match(self):
    """
    To match the value chose by user from the Option Menu,
    and return the relative value according to curr_list.
    """
    for x, y in curr_list:
        if x == self:
            return y


#make a Button Widget
def calculator(*args):
    """
    Exchange rates are scrapped from x-rates.com and saved in rates_array.
    1.obtain user's choices of currencies to exchange
    3.multiply output with corresponding rates

    For example:
    > from_curr.get() 
    "EUR"
    > to_curr.get()
    "CNY"
    > eval(input_var.get())
    100

    """
    value = eval(input_var.get())
    if from_curr.get() == to_curr.get():
        output.set(value)
    elif from_curr.get() == "USD":
        anchor = np.where(rates_array == match(to_curr.get()))
        row = anchor[0]
        output.set(value * rates_array[row][0][1].astype(float))
    elif to_curr.get() == "USD":
        anchor = np.where(rates_array == match(from_curr.get()))
        row = anchor[0]
        output.set(value * rates_array[row][0][2].astype(float))
    else:
        anchor1 = np.where(rates_array == match(from_curr.get()))
        row1 = anchor1[0]
        anchor2 = np.where(rates_array == match(to_curr.get()))
        row2 = anchor2[0]
        output.set(value * rates_array[row1][0][2].astype(float) * rates_array[row2][0][1].astype(float))


checkButton = Button(root, text="Check", command=calculator)
checkButton.grid(row=4, column=0)
root.bind('<Return>', calculator)

quitButton = Button(root, text="Exit", command=root.quit)
quitButton.grid(row=4, column=1)

root.mainloop()