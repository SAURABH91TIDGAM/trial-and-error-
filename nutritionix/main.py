import requests
import os
from datetime import datetime

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/"

exercise_endpoint = f"{nutritionix_endpoint}/exercise"

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "176"
AGE = "31"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["nutritionix_endpoint"]
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")




for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
bearer_headers = {"Authorization": f"Bearer {os.environ['TOKEN']}"}

response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
    )



    #response = requests.post(exercise_endpoint, json=sheet_inputs)

print(response.text)