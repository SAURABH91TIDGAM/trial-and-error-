import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "576wtweyt76fdcuywge87w7wefygcdg"
USERNAME= "saurabhtidgam"
GRAPH_ID= "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": USERNAME,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.now()
#
# print(TODAY)
# TODAY = f"{today.year}{today.month}{today.day}"

TODAY = datetime(year=2023, month=10, day=30)
TODAY = TODAY.strftime("20%y%m%d")
print(TODAY)

# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# pixel_data = {
#     "date": TODAY,
#     "quantity": "13.74",
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

DATE = TODAY
print(DATE)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
pixel_data = {
    "quantity": "23.74",
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

response = requests.delete(url=delete_endpoint, json=pixel_data, headers=headers)
print(response.text)
