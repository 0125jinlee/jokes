<html>
  <head>
    <title>Jo¢es</title>
    <script src="https://js.stripe.com/v3/"></script>
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
    </div>
  </body>
</html>