import sys,os
import json
from tkinter import *
import requests

# get key from https://openweathermap.org/
API_KEY="insert here"

# Send request and get back json data
def sendReq():
    zipcode=locationEntry.get()
    r=requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+'&appid='+API_KEY)
    data=r.json()
    print(data["name"])
    townName.config(text=data["name"]+" : ("+str(data["coord"]["lat"])+","+str(data["coord"]["lon"])+")")
    weatherText=""
    for x in data["weather"]:
        weatherText+=x["main"]+" "
    weatherText=weatherText.strip()
    weatherText=weatherText.replace(" ", " and ")
    weather.config(text=weatherText)
    ftemp= round((data["main"]["temp"]-273.15)*9/5+32,2)
    temp.config(text="Temperature in F°: "+str(ftemp))
    humid.config(text="Humidity: "+str(data["main"]["humidity"])+"%")
    windSpeed=round(data["wind"]["speed"]*2.237,2)
    wind.config(text="Wind Speed: "+str(windSpeed)+" mph at "+str(data["wind"]["deg"])+"°")

# Init tkinter
root=Tk()
root.title("Weather App")
root.geometry('640x480')

# Create objects and place them
l=Label(root,text="Enter your zipcode.")
locationEntry=Entry(root,width=36,text="Enter your zipcode")
enter=Button(root,text="Search",width=10,command=sendReq)
townName=Label(root, text="")
weather=Label(root, text="")
temp=Label(root, text="")
humid=Label(root, text="")
wind=Label(root, text="")

l.pack()
locationEntry.pack()
enter.pack()
townName.pack()
weather.pack()
temp.pack()
humid.pack()
wind.pack()

# Start program
root.mainloop()