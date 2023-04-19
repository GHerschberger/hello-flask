from flask import Flask

app = Flask("first_flask_app")

@app.route("/")
def index():
    return "hello World"

app.run()
