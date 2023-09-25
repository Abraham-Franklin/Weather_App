import json
import requests

city = input("Enter city: ")
api_key = "85971a067dd524d514061870d1d1502c"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

response = requests.get(url)
result = response.json()

temperature = result['list'][0]['main']['temp']
description = result['list'][0]['weather'][0]['description']
time = result['list'][0]['dt_txt'][:9]
date = result['list'][0]['dt_txt'][-8:]

print(f"City: {city} \nTemperature: {temperature} \nDescription: {description} \nTime: {time} \nDate: {date}")

#print(json.dumps(result, indent = 4, sort_keys=True))