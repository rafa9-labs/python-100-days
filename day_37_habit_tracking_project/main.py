# GET: Your program -> request data -> External System -> Response data -> Your Program ---- requests.get()
# POST: Your program -> give data -> External System -> Response status -> Your Program ---- requests.post()
# we are gonna use pixela API

import requests
import config
# Create your user account

pixela_endpoint =  "https://pixe.la/v1/users"

# Create your user account
# We send a piece of JSON data. (Only run once)
# user_params = {
#     "token": config.token, 
#     "username": config.username, 
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


pixela_graph_endpoint =  f"{pixela_endpoint}/{config.username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "Time",
    "type": "float",
    "color": "shibafu"
}

# Headers: Contain the relevant information about the sender.
headers = {
    "X-USER-TOKEN": config.token
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# To access the graph in the browser: https://pixe.la/v1/users/rafitass123/graphs/graph1.html

# It has not the same endpoint as the graphs
pixela_graph_endpoint =  f"{pixela_endpoint}/{config.username}/graphs/{config.id}"

import datetime

today = datetime.datetime(year=2026, month=2, day=7)
# today = datetime.now()

# Posting a pixel onto the graph.
pixela_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.6",
}

# response = requests.post(url=pixela_graph_endpoint, json=pixela_pixel_params, headers=headers)
# print(response.text)

# ------------------------------- # -------------------------------
# HTTP Requests: | GET | POST | PUT | DELETE |
# GET = “show me”
# Reads data.
# Should not change anything on the server.
# Examples: open a webpage, fetch your Pixela graph definition, get today’s pixel value.
# ------------------------------- # -------------------------------
# POST = “create this new thing here”
# Creates something new under a collection.
# You usually send JSON/body with the data to create.
# Examples in Pixela: create a user (POST /users), create a graph (POST /users/<u>/graphs), add a pixel (POST /users/<u>/graphs/<id> — it’s “create a new pixel entry for that date”).
# ------------------------------- # -------------------------------
# PUT = “replace/update this specific thing”
# Updates an existing resource at a specific URL (or creates it at that exact URL in some APIs).
# Idempotent: doing the same PUT twice should leave the server in the same state.
# Pixela example: update a pixel quantity for a date (PUT /graphs/<id>/<date>). If you send "quantity": "3.1" twice, the result is still 3.1.
# ------------------------------- # -------------------------------
# DELETE = “remove this”
# Deletes the resource at that URL.
# Idempotent-ish: deleting twice usually means the second time it’s already gone (some APIs return 404, others return success anyway).
# Pixela example: delete the pixel for a date (DELETE /graphs/<id>/<date>).
# ------------------------------- # -------------------------------

# Update a pixel in the graph.
pixela_update_endpoint =  f"{pixela_endpoint}/{config.username}/graphs/{config.id}/{today.strftime("%Y%m%d")}"

pixela_update_params = {
    "quantity": "3.1",
}
# response = requests.put(url=pixela_update_endpoint, json=pixela_update_params, headers=headers)
# print(response.text)

# Delete a pixel in the graph.

pixela_update_params = {
    
}

pixela_delete_endpoint =  f"{pixela_endpoint}/{config.username}/graphs/{config.id}/{today.strftime("%Y%m%d")}"
response = requests.delete(url=pixela_delete_endpoint, headers=headers)
print(response.text)
