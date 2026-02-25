import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    raise SystemExit("Missing api key")

r = requests.get("https://ipinfo.io/json")

data = r.json()
city = data["city"]

params = {
    "q": city,
    "appid": api_key,
    "units": "imperial"
}

weather_url = "https://api.openweathermap.org/data/2.5/weather"
weather_responce = requests.get(weather_url, params=params)

weather_data = weather_responce.json()

if weather_responce.status_code == 401:
    print("Invalid API Ojash do it right")

if weather_responce.status_code == 200:
    print("\nCurrent Weather\nCity: ", city,
          "\nStatus: ", weather_data["weather"][0]["main"],
          "\nStatus(id): ", weather_data["weather"][0]["id"],
          "\nFeels Like: ", weather_data["main"]["feels_like"],
          "\nTemperature: ", weather_data["main"]["temp"], "F",
          "\nBase: ", weather_data["base"])
    print("Wind Speed: ", weather_data["wind"]["speed"])

else:
    print("Error", weather_data)
