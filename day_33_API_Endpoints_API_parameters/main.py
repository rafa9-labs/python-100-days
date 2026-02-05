# API -> Application Programming Interface (API) is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with an external system.

# API endpoint -> Location where the API can be found.
# API request -> Teller, means of communication you have between you and the endpoint.

# http://api.open-notify.org/iss-now.json # Current ISS Position in terms of longitude and latitude, in JSON format.

import requests
import json


response = requests.get(
    url="http://api.open-notify.org/iss-now.json"
)
print(response) # <Response [200]>, reponse code 200, signifies success.

# Response codes: [100] - Hold On, [200] - Here you go, [300] - Go Away, [400] - You Screwed Up, [500] - I Screwed Up 
# htttpstatuses.com -> For more Response codes.

print(response.status_code) # 200 -> Successful!

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.")

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
iss_position = (latitude, longitude)

# We can use latlong.net -> to show the latitude and longitude of a certain set of coordinates.
print(iss_position)