# To run under flask, env FLASK_APP=jokes.py flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    if data["type"] == "single":
        jokes = data["joke"]
    
    elif data["type"] == "twopart":
        jokes = data["setup"] + "\n" + data["delivery"]
    
    return render_template("index.html", jokes=jokes)

# To get data from jokes API

import requests

response = requests.get("https://sv443.net/jokeapi/category/Any")

data = response.json()

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys

import stripe
# Stripe public key
stripe.api_key = 'pk_test_GoGmPnZrTiW5zxrxvKI4vjMW00YOPoShDw'
