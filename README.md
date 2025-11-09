# SMSBtc - Bitcoin Information via SMS & WhatsApp

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-3.1.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)

A simple SMS and WhatsApp interface for accessing Bitcoin price information and currency conversions. Built to provide access to Bitcoin information for populations with mobile phones but limited internet access.

## Features

- 📱 **Dual Channel Support**: Works with both SMS and WhatsApp
- 💰 Real-time Bitcoin price lookup in multiple currencies
- 💱 Currency to Bitcoin conversion
- ₿ Bitcoin to currency conversion
- 🎨 WhatsApp-enhanced formatting (emojis, bold text, better layout)
- 📊 Support for 30+ currencies via Blockchain.info API
- 🌍 No smartphone or app required (works on basic feature phones)

## Commands

Send text messages to your Twilio phone number using these commands:

| Command | Example | Description |
|---------|---------|-------------|
| `$listcurrencies` | `$listcurrencies` | Lists all supported currencies |
| `$btcprice` | `$btcprice usd` | Get Bitcoin price in USD |
| `$currencyconvert` | `$currencyconvert 100 eur` | Convert 100 EUR to Bitcoin |
| `$btcconvert` | `$btcconvert 0.01 usd` | Convert 0.01 BTC to USD |
| `$help` | `$help` | Display list of commands |
| `$about` | `$about` | Information about the project |

## Quick Start

### Prerequisites

- Python 3.12+ (Python 3.10+ should work)
- Twilio account (free trial available)
- Twilio phone number

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/richvincent/smsbtc.git
   cd smsbtc
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings (optional - defaults work fine)
   ```

5. **Run locally**
   ```bash
   python run.py
   ```
   The app will start on `http://localhost:5000`

### Twilio Setup

1. **Create a Twilio account**
   - Sign up at [twilio.com/try-twilio](https://www.twilio.com/try-twilio)
   - Get a free trial phone number

2. **Configure webhook**
   - Go to [Twilio Console → Phone Numbers](https://console.twilio.com/phone-numbers)
   - Select your phone number
   - Under "Messaging", set the webhook URL to your public app URL
   - For local development, use [ngrok](https://ngrok.com/):
     ```bash
     ngrok http 5000
     ```
   - Set webhook to: `https://your-ngrok-url.ngrok.io/`
   - Set HTTP method to `POST`

3. **Test it**
   - Send a text to your Twilio number: `$help`
   - You should receive a list of commands

### WhatsApp Setup

SMSBtc fully supports WhatsApp with enhanced formatting, emojis, and rich messaging!

#### Quick Start (Sandbox - Testing)

1. **Access WhatsApp Sandbox**
   - Go to [Twilio Console](https://console.twilio.com)
   - Navigate to Messaging → Try it out → Send a WhatsApp message

2. **Join the Sandbox**
   - Follow the instructions to join (send "join [code]" to the sandbox number)
   - Example: Send `join market-golden` to the displayed number

3. **Configure Webhook**
   - Set webhook URL to your app: `https://your-app.com/whatsapp`
   - Or use the default `/` endpoint (works for both SMS and WhatsApp)
   - Method: `POST`

4. **Test on WhatsApp**
   - Send `$help` to the sandbox number
   - You'll receive a beautifully formatted response with emojis!

#### Production Setup

For production WhatsApp Business API access:
- Apply for WhatsApp Business Account through Twilio
- Requires business verification (1-3 weeks)
- See [WHATSAPP_SETUP.md](WHATSAPP_SETUP.md) for complete guide

#### WhatsApp vs SMS

| Feature | WhatsApp | SMS |
|---------|----------|-----|
| Formatting | ✅ Rich (bold, emojis) | Plain text |
| Cost | Free for users | Carrier charges |
| Setup | Sandbox: instant, Production: 1-3 weeks | Instant |
| User Experience | Modern, visual | Basic |

📚 **Full WhatsApp guide**: See [WHATSAPP_SETUP.md](WHATSAPP_SETUP.md)

## Deployment

### Deploy to Heroku

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku

   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and create app**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Set your Twilio webhook** to `https://your-app-name.herokuapp.com/`

### Deploy to Railway

1. **Install Railway CLI**
   ```bash
   npm i -g @railway/cli
   railway login
   ```

2. **Initialize and deploy**
   ```bash
   railway init
   railway up
   ```

3. **Get your URL** and configure Twilio webhook

### Deploy to Render

1. Create account at [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
5. Configure Twilio webhook with your Render URL

## Configuration

Environment variables (optional):

```bash
# Server Configuration
PORT=5000              # Port to run the server on
DEBUG=False            # Enable Flask debug mode (True/False)

# Application Settings
MARKUP_PERCENTAGE=12.5 # Percentage markup for spot price calculations

# WhatsApp Settings
ENABLE_WHATSAPP_FORMATTING=True  # Enable emojis and rich formatting for WhatsApp
```

## Development

### Project Structure

```
smsbtc/
├── run.py              # Main Flask application (SMS + WhatsApp)
├── bitcoin_api.py      # Bitcoin price API helper
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
├── runtime.txt        # Python version specification
├── setup.sh           # Quick setup script
├── .env.example       # Environment variable template
├── .gitignore         # Git ignore rules
├── README.md          # This file
├── WHATSAPP_SETUP.md  # WhatsApp integration guide
├── DEPLOYMENT.md      # Deployment guide for multiple platforms
└── CHANGELOG.md       # Version history and changes
```

### Running Tests

```bash
# Install development dependencies
pip install pytest pytest-flask

# Run tests (when implemented)
pytest
```

### Local Development with ngrok

For local testing with Twilio:

```bash
# Terminal 1: Run the Flask app
python run.py

# Terminal 2: Start ngrok tunnel
ngrok http 5000

# Copy the ngrok HTTPS URL to your Twilio webhook configuration
```

## Architecture

- **Flask**: Lightweight Python web framework
- **Twilio**: SMS and WhatsApp messaging API
- **Blockchain.info**: Real-time Bitcoin price data
- **python-dotenv**: Environment variable management
- **gunicorn**: Production WSGI server
- **Automatic channel detection**: Seamlessly handles both SMS and WhatsApp

## API Endpoints

- `POST /` - Default webhook endpoint (handles both SMS and WhatsApp)
- `POST /message` - Generic message webhook
- `POST /whatsapp` - Dedicated WhatsApp webhook
- `POST /sms` - Dedicated SMS webhook
- `GET /health` - Health check endpoint (returns JSON status)

All POST endpoints work identically - use whichever you prefer!

## Mission

A large portion of the global population is unbanked and lacks access to global financial instruments. This same population often has access to cell service, SMS messaging, and WhatsApp. SMSBtc aims to provide access to Bitcoin information through simple messaging - no smartphone or internet browser required.

## Working Demo

Try the working example: Send a text to **+1 (313) 228-3671** with any command (e.g., `$help`)

*Note: This demo runs on free-tier hosting, so response times may vary.*

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Future Enhancements

- [ ] Unit tests with pytest
- [ ] Rate limiting per phone number
- [ ] Database for user preferences and history
- [ ] Additional cryptocurrency support (ETH, LTC, etc.)
- [ ] Price alerts via scheduled SMS
- [ ] Historical price charts via MMS
- [ ] Multi-language support

## Resources

- [Bitcoin Foundation](https://bitcoin.org)
- [Twilio Python Documentation](https://www.twilio.com/docs/libraries/python)
- [Blockchain.info API](https://www.blockchain.com/api)
- [Global Financial Inclusion (Global Findex) Database](https://www.worldbank.org/en/programs/globalfindex)
- [Wikipedia: Unbanked](https://en.wikipedia.org/wiki/Unbanked)

## Author

**Richard Vincent**

- Email: [rich@richardvincent.com](mailto:rich@richardvincent.com)
- Twitter: [@rkvincent](https://twitter.com/rkvincent)
- GitHub: [github.com/richvincent](https://github.com/richvincent)

## License

MIT License - feel free to use this project however you'd like!

## Acknowledgments

Originally created as a capstone project for Thinkful Python bootcamp. Updated in 2025 with modern dependencies and best practices.

---

**Found a bug? Please try to break it and tell me how you did it!**
