import requests
<<<<<<< HEAD
=======
from dotenv import load_dotenv
>>>>>>> d109180 (Initial commit - weather app)
import os

from datetime import datetime

<<<<<<< HEAD
api_key = "ee81424300ccd1d61a5b515831c9c5bc"
   
=======
load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

>>>>>>> d109180 (Initial commit - weather app)
if not api_key:
    raise SystemExit("Missing api key")


r = requests.get("https://ipinfo.io/json")

<<<<<<< HEAD
=======

>>>>>>> d109180 (Initial commit - weather app)
data = r.json()
city=data["city"]

params = {
    "q" : city,
    "appid" : api_key,
    "units" : "imperial"
}


<<<<<<< HEAD
=======

>>>>>>> d109180 (Initial commit - weather app)
weather_url = "https://api.openweathermap.org/data/2.5/weather"
weather_responce = requests.get(weather_url, params=params)


<<<<<<< HEAD
weather_data = weather_responce.json()

if weather_responce.status_code == 401:
    print ("Invalid API Ojash do it right")

=======

weather_data = weather_responce.json()


if weather_responce.status_code == 401:
    print ("Invalid API Ojash do it right")


>>>>>>> d109180 (Initial commit - weather app)
if weather_responce.status_code == 200:
    print("\nCurrent Weather\nCity: ", city,
          "\nStatus: ", weather_data["weather"][0]["main"],
          "\nStatus(id): ", weather_data["weather"][0]["id"],
          "\nFeels Like: ", weather_data["main"]["feels_like"],
          "\nTemperature: ", weather_data["main"]["temp"], "F",
          "\nBase: ",weather_data["base"])
    print ("Wind Speed: ", weather_data["wind"]["speed"])
<<<<<<< HEAD
else:
    print ("Error", weather_data)


=======

else:

    print ("Error", weather_data)
>>>>>>> d109180 (Initial commit - weather app)
