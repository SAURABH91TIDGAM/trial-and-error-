import json

from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 3)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess_name(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url)
    gender_data = response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess_name.html", name=name, gender=gender, age=age)

def get_blog():
    blog_url = "https://www.npoint.io/docs/c790b4d5cab58020d391"

    response = requests.get(blog_url)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Check if the response has a valid JSON content type
    print(response.headers.get("content-type", ""))
    # if "application/json" in content_type:
    #     all_posts = response.json()
    #     return render_template("blog.html", posts=all_posts)
    # else:
    #     # Handle cases where the response is not in JSON format
    #     error_message = f"Invalid content type: {content_type}. Expected JSON."
    #     return render_template("error.html", error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)