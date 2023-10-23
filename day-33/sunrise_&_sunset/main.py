import requests
import datetime as dt

today = dt.datetime.now()
date = today.date()
print(date)

parameters = {"lat": 19.033049, "lng": 73.029663, "date": f"{date}", "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise = response.json()["results"]["sunrise"]
sunrise = sunrise.split("T")[1].split(":")
sunset = response.json()["results"]["sunset"]
sunset = sunset.split("T")[1].split(":")

print(f"sunrise: {sunrise}, sunset: {sunset}")