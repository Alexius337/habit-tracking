import requests 
from datetime import datetime
import config

USERNAME = config.username
TOKEN = config.API_token
GRAPHID = config.graphID

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## response = requests.post(url=pixela_endpoint, json=user_params)
## response.raise_for_status
## print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Yoga Graph",
    "unit": "Classes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params,headers=headers)
# response.raise_for_status
# print(response.text)

## Go to URL https://pixe.la/v1/users/{username}/graphs/{graph_id}.html

## POST A NEW PIXEL

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = str(datetime.now())
date = today[0:10].replace("-", "")

pixel_data = {
    "date": date,
    "quantity": input("How many yoga classes did you do today?")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
response.raise_for_status
print(response.text)

## UPDATE A PIXEL

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

new_pixel_data = {
    "quantity": "3"
}

# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# response.raise_for_status
# print(response.text)

## DELETE PIXEL

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# response.raise_for_status
# print(response.text)