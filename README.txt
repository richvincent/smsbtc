

smsbtc

The purpose of this project is to demonstrate a simple SMS interface for
accessing Bitcoin information. The interface for this project is strictly SMS.
This project is written using the Python 3 programming language and the Flask_
(http://flask.pocoo.org/), blockchain.info_(https://blockchain.info/api), and
Twilio_twiml_(https://www.twilio.com/docs/api/twiml) API's To use the Twilio
APIs you will have to register for a trial account. Register for a free API key
here http://www.twilio.com/try-twilio A Twilio_number_(https://www.twilio.com/
phone-numbers) is required for this to work as well. run.py runs as a Flask
server. I published the project to Heroku_(http://www.heroku.com) the
application worked just fine when deployed using AWS_EC2_(https://
aws.amazon.com/ec2) as well. *Although the AWS option is a little more advanced
and complex to configure. Your public facing Flask server URL and port need to
be integrated into Twilio "Programmable SMS" messaging services request URL
field. Once the run.py is running and globally accessible the btcSMS is ready
to use.

Instructions for SMSbtc:

Commands are sent to the server via SMS messages sent to your Twilio phone
number: ie if your Twilio phone number is +12223334444 Send text messages
proceeded by the '$' symbol to the number List of valid commands:
-> $listcurrencies - Lists currencies currently supported by symbol
-> $btcprice - Lists Bitcoin price in requested currency - ie $btcprice usd
-> $currencyconvert - Converts specified currency amount to Bitcoin - ie
$currencyconvert 100.00 eur
-> $btcconvert - Converts specified amount of bitcoin to chosen currency - ie
$btcconvert .17 usd
-> $help - Returns a list of valid commands
-> $about - Returns information about author and application
*note: Any other inputs will return the help message

About

A large portion of the global population is unbanked and lacks access to global
financial instruments. This same large global unbanked population does indeed
usually have access to cell service and SMS messaging. The hope is to provide
access to the Bitcoin economy through SMS messaging. The project source code
can be located at https://github.com/richvincent/smsbtc. Please feel free to
critique, contribute, or both Author: Richard Vincent
rich@richardvincent.com
313-482-8558


References:


* Bitcoin_Foundation_Website_(http://www.bitcoin.org)
* Twilio_Python_Flask_Example_(https://www.twilio.com/docs/quickstart/python/
  sms/hello-monkey)
* Global_Findex_Database_(http://www.worldbank.org/en/programs/globalfindex)
* Wiki_article_on_the_Unbanked_(https://en.wikipedia.org/wiki/Unbanked)



Working Example

To try out a working example of this project send a text to +13132283671 use
the commands presented above. This example is using a Twilio demo account and
free tier Heroku account so performance might not be the best. Message me if
you have a issue @rkvincent / rich@richardvincent.com Please try to break it
(and tell me how you did it)
