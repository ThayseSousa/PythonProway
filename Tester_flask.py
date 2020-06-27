from flask import Flask

app = Flask(__name__)

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return "Hello, world!"
