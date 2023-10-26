import requests

api_key = "f449e17414d95d80d2c53e8c3efcd728"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather?"


parameters = {
    "lat": 19.078545,
    "lon":72.878176,
    "appid": api_key
}

response_received = requests.get(OWM_Endpoint, params=parameters)

data = response_received.json()

print(data)