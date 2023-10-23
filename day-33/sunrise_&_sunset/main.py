import requests
import datetime as dt

today = dt.datetime.now()
date = today.date()
print(date)

parameters = {"lat": 19.033049, "lng": 73.029663, "date": f"{date}", "formatted": 1}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

print(f"sunrise: {sunrise}, sunset: {sunset}")