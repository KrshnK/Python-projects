#Import required libraries
import requests     #To make HTTP requests
import json         #To convert JSON to Python dictionaries
import pyttsx3      #Text-to-speech conversion library

#Initialize text-to-speech engine
engine=pyttsx3.init()

#Get the name of city from the user
city=str(input("Enter the name of the city : "))

#Set up the API request URL
url=f"https://api.weatherapi.com/v1/current.json?key=ec21da5939e7472ea71193209230704&q={city}"

#Make the API request and convert the response to a Python dictionary
r=requests.get(url)
wdic=json.loads(r.text)

#Extract the current temperature and local time from dictionary
w=wdic["current"]["temp_c"]
x=wdic["location"]["localtime"]

#Print the weather information to the console
print(f"the current weather in {city} is {w} degrees' and localtime is {x} ")

#Speak the weather information
engine.say(f"the current weather in {city} is {w} degrees' and localtime is {x} ")
engine.runAndWait()
engine.stop()