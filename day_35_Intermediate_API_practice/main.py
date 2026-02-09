import os
import requests
from twilio.rest import Client
import config_example

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

sms_account_sid = config_example.sms_account_sid
auth_token = config_example.auth_token
weather_key = config_example.weather_key

# Extracting Location from Geocoding API.
url_geo = "http://api.openweathermap.org/geo/1.0/direct"
geo_params = {"q": "London,GB", "limit": 3, "appid": weather_key}

r = requests.get(url_geo, params=geo_params, timeout=10)
r.raise_for_status()
data = r.json()

loc = data[0]
lat, lon = loc["lat"], loc["lon"]

params = {"lat": lat, "lon": lon, "appid": weather_key, "cnt": 4}

# Extracting Weather forecast
url_weather = "https://api.openweathermap.org/data/2.5/forecast"
r = requests.get(url_weather, params=params, timeout=10)
r.raise_for_status()
data = r.json()

def check_rain():
    for entry in data.get("list", []):
        for element in entry.get("weather", []):
            wid = element.get("id")
            if wid is not None and wid < 700:
                client = Client(sms_account_sid, auth_token)
                msg = client.messages.create(
                    body="It is going to rain. Remember to bring an ☂️",
                    from_=config_example.from_number,
                    to=config_example.to_number,
                )
                print(msg.sid, msg.status)
                return

check_rain()
