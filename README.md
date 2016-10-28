smsbtc
The purpose of this project is to provide a simple SMS interface for accessing Bitcoin information.

The interface for this project is strictly SMS.

This project is written using Python 3 programming language and the Flask, blockchain.info, and Twilio twiml API's

To use the Twilio APIs you will have to register for a trial account. Register for a free API key here http://www.twilio.com/try-twilio

An Twilio number is required for this to work as well.

run.py runs as a Flask server. I published the project to Heroku but it worked fine on AWS EC2 as well.

Your public facing Flask server URL and port needs to be integrated into Twilio "Programmable SMS" messaging services request URL field.

Once the run.py is running and globally accessible the btcSMS is ready to use.

Instructions for SMSbtc:

Instructions are sent to the server via SMS commands to your Twilio phone number:

ie if your Twilio phone number is +12223334444

Send text messages proceeded by the '$' symbol to the number

List of valid commands:
-> $listcurrencies - Lists currencies currently supported by symbol
-> $btcprice - Lists Bitcoin price in requested currency - ie $btcprice usd
-> $btcconvert - Converts specified currency amount to Bitcoin - ie $btcconvert 100.00 eur
