from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
            '<p>This is a paragraph</p>'\
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGhyOWl3cnNqOHR4bXd2anVvdGFhYWd0dXJvdWh2OXptNm5pYzcyMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gNke2UrUTopOg/giphy.gif">'
@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello there { name + 12}"


if __name__ == "__main__":
    app.run(debug=True)