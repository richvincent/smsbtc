<h1>smsbtc</h1>
The purpose of this project is to demonstrate a simple SMS interface for accessing Bitcoin information.

The interface for this project is strictly SMS.

This project is written using the Python 3 programming language and the <a href="http://flask.pocoo.org/">Flask</a>, <a href="https://blockchain.info/api">blockchain.info</a>, and <a href="https://www.twilio.com/docs/api/twiml">Twilio twiml</a> API's

To use the Twilio APIs you will have to register for a trial account. Register for a free API key here http://www.twilio.com/try-twilio

A <a href="https://www.twilio.com/phone-numbers">Twilio number</a> is required for this to work as well.

run.py runs as a Flask server. I published the project to <a href="http://www.heroku.com">Heroku</a> but it worked fine on <a href="https://aws.amazon.com/ec2">AWS EC2</a> as well <em>*Although this option is a little more advanced and complex to configure.</em>

Your public facing Flask server URL and port need to be integrated into Twilio "Programmable SMS" messaging services request URL field.

Once the run.py is running and globally accessible the btcSMS is ready to use.

<h2>Instructions for SMSbtc:</h2>

Commands are sent to the server via SMS messages sent to your Twilio phone number:
ie if your Twilio phone number is <b>+12223334444</b>

Send text messages proceeded by the '$' symbol to the number

List of valid commands:<br>
-> <b>$listcurrencies</b> - Lists currencies currently supported by symbol<br>
-> <b>$btcprice</b> - Lists Bitcoin price in requested currency - ie $btcprice usd<br>
-> <b>$btcconvert</b> - Converts specified currency amount to Bitcoin - ie $btcconvert 100.00 eur<br>
-> <b>$help</b> - Returns a list of valid commands<br>
<br>
<h2>References:</h2>
<ul>
    <li><a href="https://www.twilio.com/docs/quickstart/python/sms/hello-monkey">Twilio Python Flask Example:</a></li>

