weather_data = '''{
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

for city_data in weather_data["cities"]:
    city_name = city_data["name"]
    country = city_data["country"]
    
    weather_info = city_data["weather"]
    temperature = weather_info["temperature"]["value"]
    condition = weather_info["condition"]
    description = weather_info["description"]
    
    print(f"City: {city_name}, Country: {country}")
    print(f"Temperature: {temperature} Celsius")
    print(f"Condition: {condition}")
    print(f"Description: {description}")
    print()