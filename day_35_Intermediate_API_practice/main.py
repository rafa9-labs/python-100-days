import requests
from twilio.rest import Client
import config

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

sms_account_sid = config.sms_account_sid
auth_token = config.auth_token
weather_key = config.weather_key

# Extracting Location from Geocoding API.
url_geo = "http://api.openweathermap.org/geo/1.0/direct?q=London,GB&limit=3&appid=ae5510839ccbc5651b43654e06572fe2"
r =  requests.get(url_geo, timeout=10)
r.raise_for_status()
data = r.json()
loc = data[0]
lat, lon = 39.601215, -9.070099

params = {
    "lat": lat,
    "lon": lon,
    "appid": weather_key,
    "cnt": 4,
}

# Extracting Weather with previous codes.
url_weather = "https://api.openweathermap.org/data/2.5/forecast"
r =  requests.get(url_weather, params=params, timeout=10)
r.raise_for_status()
data = r.json()

def check_rain():
    for entry in data.get("list", []):
        weather = entry["weather"]
        for element in weather:
            if element.get("id") < 700:
                client = Client(sms_account_sid, auth_token)
                message = client.messages.create(
                    body="It is going to rain. Remember to bring an ☂️",
                    from_="+15075194228",
                    to="+351937048312",
                )
                print(message.sid)
                print(message.status)
                return
    
check_rain()