import requests
from datetime import datetime
from datetime import timezone

PORTUGAL_LAT = 39.399872
PORTUGAL_LNG = 8.224454

parameters = {
    'lat': PORTUGAL_LAT,
    'lng': PORTUGAL_LNG,
    'formatted': 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()


sunrise, sunset = data.get('results')['sunrise'].split('T')[1], data.get('results')['sunset'].split('T')[1]

sunrise_time = datetime.strptime(sunrise, "%H:%M:%S%z").timetz()
sunset_time = datetime.strptime(sunset, "%H:%M:%S%z").timetz()

now_time = datetime.now(timezone.utc).timetz()

def check_daytime(sunrise, sunset, now):
    if sunrise <= now < sunset:
        print("Daytime!")
    else:
        print("Nighttime!")

check_daytime(sunrise=sunrise_time, sunset=sunset_time, now=now_time)

print(sunrise, sunset)












# print(data)
# print(sunrise, sunset)
# print(info)

