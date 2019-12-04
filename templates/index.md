<html>
  <head>
    <title>Jo¢es</title>
    <script src="https://js.stripe.com/v3/"></script>
    <script src="{{ url_for('static', filename='javascript/jokes.js') }}"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    <link href="https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz&display=swap" rel="stylesheet">
  </head>

  <body>
    <h1>JOKES OF THE DAY</h1>
    <div class="jokes">
      <h2>{{ jokes }}</h2>
      <h2>Is this joke worth ¢50? Please donate!</h2>
    </div>

    <div class="payments">
      <h2>This will be a payment box</h2>
      <form action="/charge" method="post" id="payment-form">
        <div class="form-row">
          <label for="card-element">
            Credit or debit card
          </label>
          <div id="card-element">
            <!-- A Stripe Element will be inserted here. -->
          </div>

          <!-- Used to display Element errors. -->
          <div id="card-errors" role="alert"></div>
        </div>

        <button>Submit Payment</button>
      </form>
    </div>
  </body>
</html>