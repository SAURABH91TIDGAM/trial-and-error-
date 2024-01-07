from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)