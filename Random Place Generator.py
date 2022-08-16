# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:24:09 2022

@author: PC_RC
"""

from tkinter import *
import random

root = Tk()
root.title("Random Place Generator")
root.geometry("400x400")
root.configure(background="lightblue")

enter_country_name = Entry(root)
enter_country_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)
enter_city_name = Entry(root)
enter_city_name.place(relx = 0.5, rely = 0.3, anchor = CENTER)

country_label = Label(root)
city_label = Label(root)
random_country_label = Label(root)
random_city_label = Label(root)

countrylist = []
citylist = []

def addplace():
    country_name = enter_country_name.get()
    countrylist.append(country_name)
    country_label["text"] = "Country Name: " + str(countrylist)
    
    city_name = enter_city_name.get()
    citylist.append(city_name)
    city_label["text"] = "City Name: " + str(citylist)
    
    
def randomplace():
    countrylength = len(countrylist)
    random_country_no = random.randint(0, countrylength-1)
    generated_random_country = countrylist[random_country_no]
    random_country_label["text"] = "Random Country: " + str(generated_random_country)
    
    citylength = len(citylist)
    random_city_no = random.randint(0, citylength-1)
    generated_random_city = citylist[random_city_no]
    random_city_label["text"] = "Random City: " + str(generated_random_city)
    
addplacebutton = Button(root, text = "Add Country and City", bg = 'blue',activebackground='lightblue',foreground="white", command = addplace)
addplacebutton.place(relx = 0.5, rely = 0.4, anchor = CENTER)
country_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
city_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
randomplacebutton = Button(root, text = "Random Country and City",bg = 'blue',activebackground='lightblue',foreground="white", command = randomplace)
randomplacebutton.place(relx = 0.5, rely = 0.7, anchor = CENTER)
random_country_label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
random_city_label.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()
    