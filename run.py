"""
SMSBtc - Bitcoin Information via SMS and WhatsApp
Provides Bitcoin price information and currency conversion through SMS and WhatsApp messaging.
"""
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import bitcoin_api
import logging
import os
from dotenv import load_dotenv
from typing import Tuple

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
MARKUP_PERCENTAGE = float(os.getenv('MARKUP_PERCENTAGE', '12.5'))
ENABLE_WHATSAPP_FORMATTING = os.getenv('ENABLE_WHATSAPP_FORMATTING', 'True').lower() == 'true'


def detect_channel(from_number: str) -> str:
    """
    Detect if message is from SMS or WhatsApp.

    Args:
        from_number: The 'From' field from Twilio request

    Returns:
        'whatsapp' or 'sms'
    """
    return 'whatsapp' if from_number.startswith('whatsapp:') else 'sms'


def format_message(message: str, channel: str) -> str:
    """
    Format message based on channel (add emojis/formatting for WhatsApp).

    Args:
        message: The base message
        channel: 'whatsapp' or 'sms'

    Returns:
        Formatted message
    """
    if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
        # WhatsApp supports emojis and better formatting
        return message
    else:
        # SMS - keep it plain
        # Remove emojis for SMS if any were added
        return message


def get_help_message(channel: str = 'sms') -> str:
    """Return the help message with all available commands."""
    if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
        return """*SMSBtc Commands* 📱

💰 *$listcurrencies* - View all supported currencies

📊 *$btcprice* <currency>
   Example: $btcprice usd

💱 *$currencyconvert* <amount> <currency>
   Example: $currencyconvert 100 eur

₿ *$btcconvert* <btc_amount> <currency>
   Example: $btcconvert 0.01 usd

❓ *$help* - Show this help message

ℹ️ *$about* - About this service

🔗 https://github.com/richvincent/smsbtc"""
    else:
        return """List of valid commands:
-> $listcurrencies - Lists currencies currently supported by symbol
-> $btcprice - Lists Bitcoin price in requested currency - ie $btcprice usd
-> $currencyconvert - Converts specified currency amount to Bitcoin - ie $currencyconvert 100.00 eur
-> $btcconvert - Converts specified amount of bitcoin to chosen currency - ie $btcconvert .17 usd
-> $help - Returns a list of valid commands
-> $about - Returns information about author and application
-> For further assistance visit https://github.com/richvincent/smsbtc
"""


def get_about_message(channel: str = 'sms') -> str:
    """Return information about the application and author."""
    if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
        return """*About SMSBtc* 🌍

A large portion of the global population is unbanked and lacks access to global financial instruments. 🏦

This service provides access to Bitcoin information through simple messaging - no smartphone or app required! 📲

*Mission:* Financial inclusion through accessible technology 💡

*Source:* https://github.com/richvincent/smsbtc
Contributions welcome! 🙌

*Author:* Richard Vincent
📧 rich@richardvincent.com
🐦 @rkvincent

📚 https://en.wikipedia.org/wiki/Unbanked"""
    else:
        return """A majority of the global population is unbanked and lack access to global financial instruments.
This same large global unbanked population does indeed usually have access to cell service and SMS messaging.
The hope is to provide access to the Bitcoin economy through SMS messaging.

The project source code can be located at https://github.com/richvincent/smsbtc.
Please feel free to critique, contribute, or both.

Author: Richard Vincent
rich@richardvincent.com
@rkvincent

ref: https://en.wikipedia.org/wiki/Unbanked
"""


def calculate_spot_price(base_price: float) -> float:
    """Calculate spot price with markup."""
    return round(base_price * (1 + MARKUP_PERCENTAGE / 100), 4)


def get_currency_emoji(currency: str) -> str:
    """Get emoji for common currencies (WhatsApp enhancement)."""
    currency_emojis = {
        'USD': '🇺🇸',
        'EUR': '🇪🇺',
        'GBP': '🇬🇧',
        'JPY': '🇯🇵',
        'CNY': '🇨🇳',
        'AUD': '🇦🇺',
        'CAD': '🇨🇦',
        'CHF': '🇨🇭',
        'INR': '🇮🇳',
        'BRL': '🇧🇷',
        'MXN': '🇲🇽',
        'KRW': '🇰🇷',
        'RUB': '🇷🇺',
        'SGD': '🇸🇬',
        'HKD': '🇭🇰',
        'SEK': '🇸🇪',
        'NOK': '🇳🇴',
        'DKK': '🇩🇰',
        'NZD': '🇳🇿',
        'ZAR': '🇿🇦',
    }
    return currency_emojis.get(currency.upper(), '💵')


@app.route("/", methods=['GET', 'POST'])
@app.route("/message", methods=['GET', 'POST'])
@app.route("/whatsapp", methods=['GET', 'POST'])
@app.route("/sms", methods=['GET', 'POST'])
def handle_message():
    """Handle incoming SMS and WhatsApp messages and respond with Bitcoin information."""
    resp = MessagingResponse()

    try:
        # Get request parameters
        from_number = request.form.get('From', 'Unknown')
        message_body = request.form.get('Body', '').strip()

        # Detect channel (SMS or WhatsApp)
        channel = detect_channel(from_number)

        logger.info(f"Received message via {channel.upper()} from {from_number}")

        if not message_body:
            msg = "Please send a command. Text $help for list of commands."
            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                msg = "👋 *Welcome to SMSBtc!*\n\nPlease send a command. Type *$help* for list of commands."
            resp.message(msg)
            return str(resp)

        message_parts = message_body.split()
        command = message_parts[0].lower()

        logger.info(f"Processing command '{command}' from {channel}")

        # Fetch ticker data
        try:
            ticker = bitcoin_api.get_ticker()
        except bitcoin_api.BitcoinPriceError as e:
            logger.error(f"Ticker fetch error: {e}")
            error_msg = "Sorry, unable to fetch Bitcoin prices at this time. Please try again later."
            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                error_msg = "⚠️ *Service Temporarily Unavailable*\n\nUnable to fetch Bitcoin prices right now. Please try again in a few moments."
            resp.message(error_msg)
            return str(resp)

        # Command: List currencies
        if command == '$listcurrencies':
            currencies = sorted(ticker.keys())
            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                # Group currencies by region/type for better readability
                currency_list = []
                for i in range(0, len(currencies), 6):
                    currency_list.append(', '.join(currencies[i:i+6]))
                message = f"*Supported Currencies* 💱\n\n" + '\n'.join(currency_list)
            else:
                message = f"Supported currencies: {', '.join(currencies)}"
            resp.message(message)
            return str(resp)

        # Command: Get BTC price
        elif command == '$btcprice':
            if len(message_parts) != 2:
                error_msg = "Please properly form command. ie $btcprice usd. Text $help for more info"
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = "❌ *Invalid Format*\n\nUsage: *$btcprice* <currency>\nExample: $btcprice usd"
                resp.message(error_msg)
                return str(resp)

            currency = message_parts[1].upper()
            if currency not in ticker:
                error_msg = f"Unsupported currency {currency}. Text $listcurrencies for supported options."
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = f"❌ *Unsupported Currency*\n\n{currency} is not supported.\nType *$listcurrencies* to see all options."
                resp.message(error_msg)
                return str(resp)

            btc_price = round(ticker[currency].get('15m', ticker[currency].get('last', 0)), 2)
            spot_price = calculate_spot_price(btc_price)

            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                emoji = get_currency_emoji(currency)
                message = f"""*Bitcoin Price* ₿ {emoji}

1 BTC = *{btc_price:,.2f} {currency}*

💰 Spot price (with {MARKUP_PERCENTAGE}% markup):
*{spot_price:,.2f} {currency}*"""
            else:
                message = f"1 BTC = {btc_price:,.2f} {currency}\nSpot price (with {MARKUP_PERCENTAGE}% markup): {spot_price:,.2f} {currency}"

            resp.message(message)
            return str(resp)

        # Command: Convert currency to BTC
        elif command == '$currencyconvert':
            if len(message_parts) != 3:
                error_msg = "Please properly form command. ie $currencyconvert 100 usd"
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = "❌ *Invalid Format*\n\nUsage: *$currencyconvert* <amount> <currency>\nExample: $currencyconvert 100 eur"
                resp.message(error_msg)
                return str(resp)

            try:
                amount = float(message_parts[1])
            except ValueError:
                error_msg = "Invalid amount. Please use a number. ie $currencyconvert 100 usd"
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = "❌ *Invalid Amount*\n\nPlease enter a valid number.\nExample: $currencyconvert 100 usd"
                resp.message(error_msg)
                return str(resp)

            currency = message_parts[2].upper()
            if currency not in ticker:
                error_msg = f"Unsupported currency {currency}. Text $listcurrencies for supported options."
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = f"❌ *Unsupported Currency*\n\n{currency} is not supported.\nType *$listcurrencies* to see all options."
                resp.message(error_msg)
                return str(resp)

            btc_amount = bitcoin_api.to_btc(currency, amount)
            if btc_amount is None:
                resp.message("Error converting currency. Please try again.")
                return str(resp)

            spot_price = calculate_spot_price(amount)

            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                emoji = get_currency_emoji(currency)
                message = f"""*Currency Conversion* {emoji} → ₿

{amount:,.2f} {currency} = *{btc_amount:.8f} BTC*

💰 Spot price (with {MARKUP_PERCENTAGE}% markup):
{spot_price:,.2f} {currency}"""
            else:
                message = f"{amount:,.2f} {currency} = {btc_amount:.8f} BTC\nSpot price (with {MARKUP_PERCENTAGE}% markup): {spot_price:,.2f} {currency}"

            resp.message(message)
            return str(resp)

        # Command: Convert BTC to currency
        elif command == '$btcconvert':
            if len(message_parts) != 3:
                error_msg = "Please properly form command. ie $btcconvert .17 usd"
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = "❌ *Invalid Format*\n\nUsage: *$btcconvert* <btc_amount> <currency>\nExample: $btcconvert 0.01 usd"
                resp.message(error_msg)
                return str(resp)

            try:
                btc_amount = float(message_parts[1])
            except ValueError:
                error_msg = "Invalid amount. Please use a number. ie $btcconvert .17 usd"
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = "❌ *Invalid Amount*\n\nPlease enter a valid number.\nExample: $btcconvert 0.01 usd"
                resp.message(error_msg)
                return str(resp)

            currency = message_parts[2].upper()
            if currency not in ticker:
                error_msg = f"Unsupported currency {currency}. Text $listcurrencies for supported options."
                if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                    error_msg = f"❌ *Unsupported Currency*\n\n{currency} is not supported.\nType *$listcurrencies* to see all options."
                resp.message(error_msg)
                return str(resp)

            fiat_amount = bitcoin_api.to_fiat(currency, btc_amount)
            if fiat_amount is None:
                resp.message("Error converting Bitcoin. Please try again.")
                return str(resp)

            spot_price = calculate_spot_price(fiat_amount)

            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                emoji = get_currency_emoji(currency)
                message = f"""*Bitcoin Conversion* ₿ → {emoji}

{btc_amount:.8f} BTC = *{fiat_amount:,.2f} {currency}*

💰 Spot price (with {MARKUP_PERCENTAGE}% markup):
{spot_price:,.2f} {currency}"""
            else:
                message = f"{btc_amount:.8f} BTC = {fiat_amount:,.2f} {currency}\nSpot price (with {MARKUP_PERCENTAGE}% markup): {spot_price:,.2f} {currency}"

            resp.message(message)
            return str(resp)

        # Command: Help
        elif command == "$help":
            resp.message(get_help_message(channel))
            return str(resp)

        # Command: About
        elif command == "$about":
            resp.message(get_about_message(channel))
            return str(resp)

        # Unknown command
        else:
            if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
                message = f"❌ *Unknown Command*\n\n_{message_body}_\n\n{get_help_message(channel)}"
            else:
                message = f"Unknown command. {get_help_message(channel)}"
            resp.message(message)
            return str(resp)

    except Exception as e:
        logger.error(f"Error processing message: {e}", exc_info=True)
        error_msg = "An error occurred processing your request. Please try again later."
        if channel == 'whatsapp' and ENABLE_WHATSAPP_FORMATTING:
            error_msg = "⚠️ *Error*\n\nSomething went wrong. Please try again later."
        resp.message(error_msg)
        return str(resp)


@app.route("/health", methods=['GET'])
def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "smsbtc",
        "channels": ["sms", "whatsapp"],
        "version": "2.1.0"
    }, 200


if __name__ == "__main__":
    # Get port from environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'

    logger.info(f"Starting SMSBtc on port {port}")
    logger.info(f"WhatsApp formatting: {'Enabled' if ENABLE_WHATSAPP_FORMATTING else 'Disabled'}")
    app.run(host='0.0.0.0', port=port, debug=debug)
