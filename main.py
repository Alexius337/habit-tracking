import requests 
import config

USERNAME = config.username
TOKEN = config.API_token

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
    "id": "graph1",
    "name": "Yoga Graph",
    "unit": "Classes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params,headers=headers)
response.raise_for_status
print(response.text)

## Go to URL https://pixe.la/v1/users/{username}/graphs/{graph_id}.html

