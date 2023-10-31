import requests
from datetime import datetime

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/"

exercise_endpoint = f"{nutritionix_endpoint}/exercise"

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "176"
AGE = "31"

APP_ID = "1153ebf8"
API_KEY = "d979a9220f30f720fed3d8e0cfa5971d"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/1c3bc1224c991eee4a08a6f5942a2b60/myWorkouts/workouts"
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

    bearer_headers = {
        "Authorization": "Bearer sheety_token@for*google#spreadsheet"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)