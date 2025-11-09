# SMSBtc - Bitcoin Information via SMS & WhatsApp

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-3.1.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-2.1.0-orange)

> **Access Bitcoin prices and conversions through simple text messages - no smartphone, app, or internet browser required.**

A messaging-based interface for Bitcoin information, supporting both SMS and WhatsApp. Designed for financial inclusion - serving populations with basic mobile phones but limited access to traditional banking infrastructure.

---

## 🆕 What's New (v2.1.0 - November 2025)

**Major Modernization** - Completely updated from 2016 codebase:
- ✅ **WhatsApp Support** - Full Business API integration with rich formatting
- ✅ **Python 3.12** - Updated from Python 3.5 (8+ years of improvements)
- ✅ **Modern Dependencies** - Flask 3.1, Twilio 9.3, latest security patches
- ✅ **Production Ready** - Logging, error handling, multiple deployment options
- ✅ **Auto-Setup** - One-command installation script

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

---

## ✨ Features

### Core Functionality
- 📱 **Dual Channel Support** - Works seamlessly with both SMS and WhatsApp
- 💰 **Real-time Bitcoin Prices** - Current BTC prices in 30+ currencies
- 💱 **Currency Conversions** - Convert any amount between fiat and Bitcoin
- 🌍 **Global Accessibility** - No smartphone, app, or internet required
- 🔄 **Automatic Channel Detection** - App detects and optimizes for SMS or WhatsApp
- 🎨 **Rich WhatsApp Formatting** - Emojis, bold text, country flags

### Technical Highlights
- 🚀 **Modern Python 3.12** with type hints and async support
- 🔒 **Environment-based Configuration** - Secure credential management
- 📊 **Comprehensive Logging** - Track usage and debug issues
- 🏥 **Health Check Endpoint** - Monitor service status
- ⚡ **Production WSGI Server** - Gunicorn for reliable hosting
- 📦 **Easy Deployment** - Guides for 6+ hosting platforms

---

## 📲 Example Usage

### SMS Experience (Plain Text)
```
You: $btcprice usd

Bot: 1 BTC = 94,567.00 USD
Spot price (with 12.5% markup): 106,387.88 USD
```

### WhatsApp Experience (Rich Formatting)
```
You: $btcprice usd

Bot: *Bitcoin Price* ₿ 🇺🇸

1 BTC = *94,567.00 USD*

💰 Spot price (with 12.5% markup):
*106,387.88 USD*
```

**Same commands, automatically optimized presentation!**

---

## 🎯 Commands

| Command | Example | Description |
|---------|---------|-------------|
| `$listcurrencies` | `$listcurrencies` | View all supported currencies |
| `$btcprice` | `$btcprice usd` | Get current Bitcoin price |
| `$currencyconvert` | `$currencyconvert 100 eur` | Convert fiat to Bitcoin |
| `$btcconvert` | `$btcconvert 0.01 usd` | Convert Bitcoin to fiat |
| `$help` | `$help` | Show command list |
| `$about` | `$about` | About this service |

**Supported Currencies**: USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, BRL, MXN, KRW, and 20+ more.

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone repository
git clone https://github.com/richvincent/smsbtc.git
cd smsbtc

# Run setup script (creates venv, installs deps, configures env)
./setup.sh

# Start server
python run.py
```

### Option 2: Manual Setup

```bash
# Clone repository
git clone https://github.com/richvincent/smsbtc.git
cd smsbtc

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure (optional)
cp .env.example .env

# Run
python run.py
```

Server starts at `http://localhost:5000`

---

## 📱 Channel Setup

### SMS Setup (Twilio)

**1. Create Twilio Account**
- Sign up at [twilio.com/try-twilio](https://www.twilio.com/try-twilio)
- Get a free phone number

**2. Configure Webhook**
- Twilio Console → Phone Numbers → Select your number
- **Messaging Webhook**: `https://your-app-url.com/`
- **Method**: `POST`
- Save

**3. Test**
- Text your Twilio number: `$help`
- You'll receive the command list!

### WhatsApp Setup (Twilio Business API)

**Quick Test (Sandbox - Instant)**
1. Twilio Console → Messaging → Try WhatsApp
2. Send join code to sandbox number (e.g., `join market-golden`)
3. Configure webhook: `https://your-app-url.com/whatsapp`
4. Test: Send `$help` via WhatsApp

**Production Setup**
- Apply for WhatsApp Business Account (requires verification)
- Approval takes 1-3 weeks
- See [WHATSAPP_SETUP.md](WHATSAPP_SETUP.md) for complete guide

**WhatsApp Benefits**
- ✅ Free for users (data vs SMS charges)
- ✅ Rich formatting with emojis and bold text
- ✅ Read receipts and delivery confirmations
- ✅ 2+ billion global users

---

## ☁️ Deployment

Deploy to your preferred platform in minutes:

### Recommended Platforms

**Railway** (Free tier, easiest)
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

**Render** (Free tier, reliable)
1. Connect GitHub repo at [render.com](https://render.com)
2. Build: `pip install -r requirements.txt`
3. Start: `gunicorn run:app`

**Heroku** (Starting at $5/month)
```bash
heroku create your-app-name
git push heroku main
```

### Other Options
- DigitalOcean App Platform ($5/month)
- AWS Elastic Beanstalk
- Google Cloud Run (serverless)

📚 **Full deployment guides**: See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## ⚙️ Configuration

Create `.env` file (optional - defaults work fine):

```bash
# Server Configuration
PORT=5000
DEBUG=False

# Application Settings
MARKUP_PERCENTAGE=12.5  # Spot price markup

# WhatsApp Features
ENABLE_WHATSAPP_FORMATTING=True  # Rich formatting for WhatsApp
```

---

## 🏗️ Architecture

### Tech Stack
- **Python 3.12** - Modern, fast, secure
- **Flask 3.1** - Lightweight web framework
- **Twilio API** - SMS and WhatsApp messaging
- **Blockchain.info API** - Real-time Bitcoin prices
- **Gunicorn** - Production WSGI server
- **python-dotenv** - Environment management

### Project Structure
```
smsbtc/
├── run.py              # Main Flask app (SMS + WhatsApp handler)
├── bitcoin_api.py      # Bitcoin price API client
├── requirements.txt    # Python dependencies
├── setup.sh           # Automated setup script
├── .env.example       # Configuration template
├── Procfile           # Production deployment config
├── runtime.txt        # Python version specification
├── README.md          # This file
├── WHATSAPP_SETUP.md  # WhatsApp integration guide
├── DEPLOYMENT.md      # Deployment instructions
└── CHANGELOG.md       # Version history
```

### API Endpoints
- `POST /` - Main webhook (auto-detects SMS/WhatsApp)
- `POST /sms` - Dedicated SMS endpoint
- `POST /whatsapp` - Dedicated WhatsApp endpoint
- `POST /message` - Generic message endpoint
- `GET /health` - Health check (monitoring)

All POST endpoints work identically - the app automatically detects the channel!

---

## 🧪 Local Testing

Test webhooks locally using ngrok:

```bash
# Terminal 1: Start app
python run.py

# Terminal 2: Start tunnel
ngrok http 5000

# Use ngrok HTTPS URL in Twilio webhook config
# Example: https://abc123.ngrok.io/
```

---

## 🌍 Mission & Impact

### The Problem
- **1.4 billion adults** are unbanked globally
- Many lack access to traditional financial services
- Most have basic mobile phones with SMS/WhatsApp

### Our Solution
Provide Bitcoin information access via universal messaging:
- ✅ No smartphone needed (works on feature phones)
- ✅ No app installation required
- ✅ No internet browser needed
- ✅ Works via SMS or WhatsApp
- ✅ Simple command-based interface
- ✅ 30+ currency support

**Target Users**: Populations in developing regions, refugees, migrant workers, rural communities - anyone with a phone but limited banking access.

---

## 🤝 Contributing

Contributions welcome! Ways to help:

- 🐛 **Report bugs** - Open an issue
- 💡 **Suggest features** - Share your ideas
- 📝 **Improve docs** - Fix typos, clarify instructions
- 🔧 **Submit PRs** - Add features or fixes
- 🌍 **Translate** - Help make it multilingual
- ⭐ **Star this repo** - Show your support!

---

## 🛣️ Roadmap

### Short Term
- [ ] Unit tests with pytest
- [ ] Rate limiting per phone number
- [ ] Request validation (Twilio signature verification)
- [ ] Caching layer (Redis) for API responses

### Medium Term
- [ ] Database integration (user preferences, history)
- [ ] Additional cryptocurrencies (ETH, LTC, XRP)
- [ ] Multi-language support (Spanish, French, Hindi)
- [ ] Price alerts via scheduled messages

### Long Term
- [ ] WhatsApp interactive buttons
- [ ] Historical price charts (MMS/WhatsApp media)
- [ ] Voice integration for accessibility
- [ ] Full custodial wallet functionality

See [GitHub Issues](https://github.com/richvincent/smsbtc/issues) for active discussions.

---

## 📊 Comparison: SMS vs WhatsApp

| Feature | WhatsApp | SMS |
|---------|----------|-----|
| **User Cost** | Free (uses data) | Carrier charges apply |
| **Formatting** | Rich (bold, emoji, flags) | Plain text only |
| **Message Length** | 4,096 characters | 160 chars (splits) |
| **Media Support** | Images, docs, audio | Limited (MMS) |
| **Read Receipts** | ✅ Yes | ❌ No |
| **Global Reach** | 2+ billion users | Universal |
| **Setup Complexity** | Medium (needs approval) | Easy (instant) |
| **Twilio Cost** | $0.005-0.03/conversation | $0.0075/message |

**Both channels work simultaneously with the same backend!**

---

## 📚 Documentation

- **[README.md](README.md)** - This file (overview & quick start)
- **[WHATSAPP_SETUP.md](WHATSAPP_SETUP.md)** - Complete WhatsApp integration guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment instructions for 6+ platforms
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates

---

## 🧑‍💻 Author

**Richard Vincent**

- 📧 Email: [rich@richardvincent.com](mailto:rich@richardvincent.com)
- 🐦 Twitter: [@rkvincent](https://twitter.com/rkvincent)
- 💼 GitHub: [github.com/richvincent](https://github.com/richvincent)

---

## 📄 License

**MIT License** - Use this project however you'd like!

See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Originally created as a capstone project for **Thinkful Python Bootcamp** (2016)
- Completely modernized in **2025** with current best practices
- Built with ❤️ for financial inclusion

---

## 📞 Support & Resources

### Need Help?
- 📖 Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment issues
- 📖 Check [WHATSAPP_SETUP.md](WHATSAPP_SETUP.md) for WhatsApp setup
- 🐛 Open an [Issue](https://github.com/richvincent/smsbtc/issues)
- 📧 Email: [rich@richardvincent.com](mailto:rich@richardvincent.com)

### Useful Links
- [Bitcoin Foundation](https://bitcoin.org)
- [Twilio Python Docs](https://www.twilio.com/docs/libraries/python)
- [Blockchain.info API](https://www.blockchain.com/api)
- [Global Financial Inclusion Database](https://www.worldbank.org/en/programs/globalfindex)
- [Wikipedia: Unbanked](https://en.wikipedia.org/wiki/Unbanked)

### Try the Demo
**Working demo available**: Text `$help` to **+1 (313) 228-3671**

*Note: Demo runs on free-tier hosting, so first response may be slow.*

---

## ⚡ Quick Command Reference

```
$listcurrencies          → View all supported currencies
$btcprice usd           → Get Bitcoin price in USD
$currencyconvert 100 eur → Convert 100 EUR to BTC
$btcconvert 0.01 usd    → Convert 0.01 BTC to USD
$help                   → Show all commands
$about                  → Learn about the project
```

---

<div align="center">

**Found a bug? Please try to break it and tell me how you did it!** 🔍

⭐ **Star this repo** if you find it useful!

🚀 **Built with Python, Flask, and a mission for financial inclusion**

</div>
