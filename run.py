from flask import Flask, request, redirect
from blockchain import exchangerates
import twilio.twiml
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    if message_body == '$btcprice':
        ticker = exchangerates.get_ticker()
        btc_price = ticker['USD'].p15min
        message_body = 'The price for 1 bitcoin in USD is {}'.format(btc_price)

    resp = twilio.twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    # Bind to Port if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
