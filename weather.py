import requests
from config import API_KEY
import savedPhrases

api_key = API_KEY  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

if "what is the weather" in querry:
    querry = savedPhrases.takecommand()
    city_name = input("Enter city name : ")
    # This is to complete the base_url, you can also do this manually to checkout other weather data available
    complete_url = base_url + "appid=" + \
        'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        weather_description = z[0]["description"]

        print(" Temperature = " +
              str(current_temperature) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")
