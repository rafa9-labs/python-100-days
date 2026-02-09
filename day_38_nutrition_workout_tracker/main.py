import requests
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

workout_base_endpoint = "https://app.100daysofpython.dev"

query = input("Tell me what exercises did you do:")

req_params = {
  "query": query,
  "weight_kg": 76,                  # Optional: Weight in kg (1-500)
  "height_cm": 175,                 # Optional: Height in cm (1-300)
  "age": 23,                        # Optional: Age (1-150)
  "gender": "male"                  # Optional: "male" or "female"
}

headers = {
    "x-app-id": os.environ["API_ID"],
    "x-app-key": os.environ["API_key"],
}

# Get the response/information about a certain exercise.
workout_information_endpoint = f"{workout_base_endpoint}/v1/nutrition/natural/exercise"
request_workout = requests.post(url=workout_information_endpoint, json=req_params, headers=headers)
print(request_workout.text)

payload = request_workout.json()          # dict
data = payload.get("exercises")
exercise = data[0].get("name")
print(exercise)
duration = data[0].get("duration_min")
print(duration)
calories = data[0].get("nf_calories")
print(calories)

from datetime import datetime
now = datetime.now()

sheety_headers = {
    "Authorization": os.environ["autorization_bearer_key"],
}

sheety_params = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}

from requests.auth import HTTPBasicAuth

print("POST_ENDPOINT:", os.environ["POST_ENDPOINT"])
print("Auth header starts with:", sheety_headers["Authorization"][:20], "...")

r = requests.post(
    url=os.environ["POST_ENDPOINT"],
    json=sheety_params,
    headers=sheety_headers,
)
print(r.status_code)
print(r.text)

g = requests.get(url=os.environ["GET_ENDPOINT"], headers=sheety_headers)
print("GET:", g.status_code)
print(g.text)