import requests
import json
import pyttsx3

engine=pyttsx3.init()

city=str(input("Enter the name of the city : "))
url=f"https://api.weatherapi.com/v1/current.json?key=ec21da5939e7472ea71193209230704&q={city}"
r=requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
x=wdic["location"]["localtime"]
print(f"the current weather in {city} is {w} degrees' and localtime is {x} ")
engine.say(f"the current weather in {city} is {w} degrees' and localtime is {x} ")
engine.runAndWait()
engine.stop()