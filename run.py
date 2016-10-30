from flask import Flask, request
from blockchain import exchangerates
import twilio.twiml
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    message_parts = message_body.split()
    resp = twilio.twiml.Response()
    ticker = exchangerates.get_ticker()
    sms_command = message_parts[0]
    help_message = """List of valid commands:
        -> $listcurrencies - Lists currencies currently supported by symbol
        -> $btcprice - Lists Bitcoin price in requested currency - ie $btcprice usd
        -> $currencyconvert - Converts specified currency amount to Bitcoin - ie $currencyconvert 100.00 eur
        -> $help - Returns a list of valid commands
        -> $about - Returns information about author and application
        -> For further assistance call or text 313-482-8558
        """


    if sms_command == '$listcurrencies':
        message_body = str(list(ticker))
        resp.message(message_body)
        return(str(resp))

    if sms_command == '$btcprice':
        if len(message_parts) != 2:
            message_body = "Please properly form command. ie $btcprice usd. Please enter $help for more info"
            resp.message(message_body)
            return(str(resp))
        sms_currency = message_parts[1].upper()
        if sms_currency in ticker:
            btc_price = round(ticker[sms_currency].p15min,4)
            spot_price = round(btc_price*1.125,4)
            message_body = "The price for 1 bitcoin is {} {}. The spot price for btc purchase is {} {}".format(btc_price, sms_currency, spot_price, sms_currency)
            resp.message(message_body)
            return(str(resp))
        else:
            message_body = "Unsupported currency {}".format(sms_currency)
            resp.message(message_body)
            return(str(resp))

    if sms_command == '$currencyconvert':
        if len(message_parts) != 3:
            message_body = "Please properly form command. $currencyconvert <amount as integer or float"
            resp.message(message_body)
            return(str(resp))
        sms_amount = message_parts[1]
        try:
            sms_amount = float(sms_amount)
        except ValueError:
            message_body = "Please properly form command. $currencyconvert <amount as integer or float"
            resp.message(message_body)
            return(str(resp))
        sms_currency = message_parts[2].upper()
        if sms_currency in ticker:
            btc_amount = round(exchangerates.to_btc(sms_currency, sms_amount),4)
            spot_price = round(sms_amount*1.125,4)
            message_body = "{} {} = {} btc; {} {} spot price for purchase of this amount of bticoin".format(sms_amount, sms_currency, btc_amount, spot_price, sms_currency)
            resp.message(message_body)
            return(str(resp))
        else:
            message_body = "Unsupported currency {}".format(sms_currency)
            resp.message(message_body)
            return(str(resp))

    if sms_command == '$btcconvert':
        if len(message_parts) != 3:
            message_body = "Please properly form command. $btcconvert <amount as integer or float"
            resp.message(message_body)
            return(str(resp))
        sms_amount = message_parts[1]
        try:
            sms_amount = float(sms_amount)
        except ValueError:
            message_body = "Please properly form command. $btcconvert <amount as integer or float"
            resp.message(message_body)
            return(str(resp))
        sms_currency = message_parts[2].upper()
        if sms_currency in ticker:
            btc_price = ticker[sms_currency].p15min
            btc_convert = round(btc_price*sms_amount,4)
            spot_price = round(btc_convert*1.125,4)
            message_body = "{} btc = {} {}; {} {} spot price for purchase of this amount of bticoin".format(sms_amount, btc_convert, sms_currency, spot_price, sms_currency)
            resp.message(message_body)
            return(str(resp))
        else:
            message_body = "Unsupported currency {}".format(sms_currency)
            resp.message(message_body)
            return(str(resp))

    if sms_command == "$help":
        message_body = help_message
        resp.message(message_body)
        return(str(resp))


    if sms_command == "$about":
        message_body = """ A majority of the global population is unbanked and lack access to global financial instruments.
        This same large global unbanked population does indeed usually have access to cell service and SMS messaging.
        The hope is to provide access to the Bitcoin economy through SMS messaging.

        The project source code can be located at https://github.com/richvincent/smsbtc. Please feel free to critique, contribute, or both

        Author: Richard Vincent
        rich@richardvincent.com
        @rkvincent
        313-482-8558

        ref: https://en.wikipedia.org/wiki/Unbanked
        """
        resp.message(message_body)
        return(str(resp))

    message_body = help_message
    resp.message('Hello {}, {}'.format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    # Bind to Port if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
