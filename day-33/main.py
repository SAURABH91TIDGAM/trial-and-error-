import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception("the resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("you are not authorised to access the data")

response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)