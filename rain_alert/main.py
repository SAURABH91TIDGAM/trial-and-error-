import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client = TwilioHttpClient(proxy={'http': os.environ["http_proxy"], 'https': os.environ["https_proxy"]})

api_key = "f449e17414d95d80d2c53e8c3efcd728"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = 'AC4570fa63efab1b73363b811aa4673cd3'
auth_token = "211248edecae245b8c6e88ee3907500c"

parameters = {
    "lat": 25.0330,
    "lon": 121.5654,
    "appid": api_key
}

response_received = requests.get(OWM_Endpoint, params=parameters)
response_received.raise_for_status()

weather_data = response_received.json()
weather_slice = weather_data["weather"][0]

print(weather_slice)


will_rain = False

for main in weather_slice:
    condition_code = weather_slice['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella.")

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It is going to rain today. Remember to bring an Umbrella.",
        from_='+731613912',
        to='++918878530091'
    )

