import json

json_weather = '''{
  "cities": [
    {
      "name": "New York",
      "country": "USA",
      "weather": {
        "temperature": {
          "value": 20,
          "unit": "Celsius"
        },
        "condition": "Clear",
        "description": "Sunny with clear skies"
      }
    },
    {
      "name": "London",
      "country": "UK",
      "weather": {
        "temperature": {
          "value": 15,
          "unit": "Celsius"
        },
        "condition": "Partly Cloudy",
        "description": "Partly cloudy with a chance of showers"
      }
    },
    {
      "name": "Paris",
      "country": "France",
      "weather": {
        "temperature": {
          "value": 25,
          "unit": "Celsius"
        },
        "condition": "Sunny",
        "description": "Sunny and warm"
      }
    },
    {
      "name": "Tokyo",
      "country": "Japan",
      "weather": {
        "temperature": {
          "value": 28,
          "unit": "Celsius"
        },
        "condition": "Rain",
        "description": "Light rain showers"
      }
    },
    {
      "name": "Sydney",
      "country": "Australia",
      "weather": {
        "temperature": {
          "value": 22,
          "unit": "Celsius"
        },
        "condition": "Cloudy",
        "description": "Overcast skies"
      }
    },
    {
      "name": "Rio de Janeiro",
      "country": "Brazil",
      "weather": {
        "temperature": {
          "value": 30,
          "unit": "Celsius"
        },
        "condition": "Sunny",
        "description": "Hot and sunny"
      }
    },
    {
      "name": "Cape Town",
      "country": "South Africa",
      "weather": {
        "temperature": {
          "value": 18,
          "unit": "Celsius"
        },
        "condition": "Windy",
        "description": "Strong winds in the afternoon"
      }
    },
    {
      "name": "Dubai",
      "country": "UAE",
      "weather": {
        "temperature": {
          "value": 35,
          "unit": "Celsius"
        },
        "condition": "Clear",
        "description": "Hot and clear skies"
      }
    },
    {
      "name": "Moscow",
      "country": "Russia",
      "weather": {
        "temperature": {
          "value": 10,
          "unit": "Celsius"
        },
        "condition": "Snow",
        "description": "Heavy snowfall expected"
      }
    },
    {
      "name": "Beijing",
      "country": "China",
      "weather": {
        "temperature": {
          "value": 22,
          "unit": "Celsius"
        },
        "condition": "Fog",
        "description": "Dense fog in the morning"
      }
    }
  ]
}'''


weather_dict = json.loads(json_weather)

print(weather_dict['cities'][0]["country"])
for key, value in weather_dict.items():
    for key2 in value:
        print(key2)
        print("================")
        print(f"country: {key2['country']}")
        print(f"Temperature: {key2['weather']['temperature']['value']} {key2['weather']['temperature']['unit']}")
        print(f"It will be {key2['weather']['description']}")
        print("+++++++++++++++++ \n\n")