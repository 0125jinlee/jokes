# To run under flask, env FLASK_APP=jokes.py flask run

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if data["type"] == "single":
        jokes = data["joke"]
    
    elif data["type"] == "twopart":
        jokes = data["setup"] + "\n" + data["delivery"]
    
    return render_template("index.html", jokes=jokes, key=stripe_keys['publishable_key'])

# To get data from jokes API

import requests

response = requests.get("https://sv443.net/jokeapi/category/Any")

data = response.json()

# To get the key from stored in os and assign it to stripe.api_key

import os

import stripe

stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

# Need to export to OS everytime terminal reboots 
# export STRIPE_PUBLISHABLE_KEY="pk_test_GoGmPnZrTiW5zxrxvKI4vjMW00YOPoShDw"
# export STRIPE_SECRET_KEY=""

stripe.api_key = stripe_keys['secret_key']

@app.route('/charge', methods=['POST'])
def charge():
    try:
        # amount in cents
        amount = 50

        customer = stripe.Customer.create(
            email='sample@customer.com',
            source=request.form['stripeToken']
        )

        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Flask Charge'
        )

        return render_template('charges.html', amount=amount)
    
    except stripe.error.StripeError:
        
        return render_template('error.html')

