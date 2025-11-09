# WhatsApp Integration Setup Guide

This guide walks you through setting up WhatsApp Business API integration for SMSBtc using Twilio.

## Table of Contents

- [Quick Start (Sandbox)](#quick-start-sandbox)
- [Production Setup](#production-setup)
- [Features](#features)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

---

## Quick Start (Sandbox)

The WhatsApp Sandbox lets you test immediately without approval. Perfect for development!

### Prerequisites

- Twilio account (free tier works)
- SMSBtc app deployed and running
- WhatsApp installed on your phone

### Step 1: Access WhatsApp Sandbox

1. **Login to Twilio Console**
   - Visit https://console.twilio.com

2. **Navigate to WhatsApp Sandbox**
   - Click "Messaging" in left sidebar
   - Click "Try it out" → "Send a WhatsApp message"
   - You'll see the sandbox configuration page

### Step 2: Join the Sandbox

1. **Get your join code**
   - Twilio displays a message like: "join [code]-[word]"
   - Example: "join market-golden"

2. **Send join message**
   - Open WhatsApp on your phone
   - Send a message to the Twilio sandbox number (shown on screen)
   - Message content: `join [your-code]`
   - Example: Send `join market-golden` to `+1 415 523 8886`

3. **Confirmation**
   - You'll receive a confirmation message in WhatsApp
   - You're now connected to the sandbox!

### Step 3: Configure Webhook

1. **Get your app URL**
   - If deployed: `https://your-app.herokuapp.com` (or your platform)
   - If local with ngrok: `https://abc123.ngrok.io`

2. **Set webhook in Twilio**
   - In the Sandbox Configuration page
   - Under "When a message comes in"
   - Enter: `https://your-app-url/whatsapp` (or just `/` works too)
   - Method: `POST`
   - Click "Save"

### Step 4: Test It!

1. **Send a test command**
   - In WhatsApp, message the Twilio sandbox number
   - Send: `$help`

2. **Expected response**
   - You should receive a nicely formatted message with emojis!
   - Example:

```
*SMSBtc Commands* 📱

💰 *$listcurrencies* - View all supported currencies

📊 *$btcprice* <currency>
   Example: $btcprice usd

💱 *$currencyconvert* <amount> <currency>
   Example: $currencyconvert 100 eur

₿ *$btcconvert* <btc_amount> <currency>
   Example: $btcconvert 0.01 usd

❓ *$help* - Show this help message

ℹ️ *$about* - About this service

🔗 https://github.com/richvincent/smsbtc
```

3. **Try a price check**
   - Send: `$btcprice usd`
   - You'll get a formatted Bitcoin price!

---

## Production Setup

For production use, you need an approved WhatsApp Business Account.

### Prerequisites

- Active business
- Facebook Business Manager account
- Approved business verification
- Twilio account (paid plan recommended)

### Step 1: WhatsApp Business Account

1. **Apply for WhatsApp Business API**
   - Go to Twilio Console → Messaging → WhatsApp
   - Click "Request to enable my Twilio numbers for WhatsApp"

2. **Provide business information**
   - Business name (must match legal entity)
   - Business website
   - Business description
   - Business address
   - Business category

3. **Facebook Business Manager**
   - Link your Facebook Business Manager
   - Complete business verification
   - This can take 1-3 weeks

### Step 2: WhatsApp Number

1. **Choose a number**
   - Use existing Twilio number, or
   - Purchase new number specifically for WhatsApp

2. **Enable WhatsApp**
   - In Twilio Console
   - Select your phone number
   - Enable "WhatsApp" capability
   - Wait for approval (usually 24-48 hours)

### Step 3: Configure Webhooks

1. **Set incoming webhook**
   - Phone Numbers → Your WhatsApp number
   - Under "Messaging"
   - When a message comes in: `https://your-app.com/whatsapp`
   - Method: `POST`

2. **Optional: Status callback**
   - Status callback URL: `https://your-app.com/status` (if you implement this)
   - This tracks message delivery status

### Step 4: Message Templates

For outbound messages (outside 24-hour window), you need pre-approved templates.

1. **Create templates**
   - Twilio Console → Messaging → WhatsApp → Templates
   - Examples:
     - Price alerts
     - Confirmations
     - Welcome messages

2. **Get approval**
   - Submit templates for WhatsApp approval
   - Usually approved within hours
   - Must follow WhatsApp policies (no spam, clear opt-out)

### Step 5: Go Live

1. **Test thoroughly**
   - Test all commands
   - Verify error handling
   - Check message formatting

2. **Promote your WhatsApp number**
   - Add to website
   - Social media
   - Marketing materials
   - Use WhatsApp business link: `https://wa.me/1234567890`

---

## Features

### What SMSBtc Supports on WhatsApp

#### ✅ Automatic Channel Detection
- App automatically detects SMS vs WhatsApp
- No code changes needed per channel

#### ✅ Enhanced Formatting (WhatsApp only)
- **Emojis**: Currency flags (🇺🇸 🇪🇺 🇬🇧), Bitcoin symbol (₿)
- **Bold text**: Important info stands out
- **Better layout**: Multi-line formatting
- **Visual hierarchy**: Headers and sections

#### ✅ All Commands Work
- `$btcprice` - Get Bitcoin price with rich formatting
- `$currencyconvert` - Convert with visual currency indicators
- `$btcconvert` - Bitcoin conversion with emojis
- `$listcurrencies` - Organized currency list
- `$help` - Beautiful help menu
- `$about` - Formatted about page

#### ✅ SMS Backward Compatible
- SMS users get plain text (no emojis)
- Same functionality, different presentation
- Both channels work simultaneously

### Example: WhatsApp vs SMS Response

**Command**: `$btcprice usd`

**WhatsApp Response**:
```
*Bitcoin Price* ₿ 🇺🇸

1 BTC = *94,567.00 USD*

💰 Spot price (with 12.5% markup):
*106,387.88 USD*
```

**SMS Response**:
```
1 BTC = 94,567.00 USD
Spot price (with 12.5% markup): 106,387.88 USD
```

---

## Testing

### Local Testing with ngrok

1. **Start your app**
   ```bash
   python run.py
   ```

2. **Start ngrok**
   ```bash
   ngrok http 5000
   ```

3. **Configure Twilio**
   - Use the ngrok HTTPS URL
   - Update sandbox webhook

4. **Test in WhatsApp**
   - Send commands to sandbox number
   - Check logs in terminal

### Testing Checklist

- [ ] Join sandbox successfully
- [ ] `$help` shows formatted help
- [ ] `$btcprice usd` returns price with formatting
- [ ] `$currencyconvert 100 eur` works correctly
- [ ] `$btcconvert 0.01 usd` converts properly
- [ ] `$listcurrencies` shows organized list
- [ ] `$about` displays formatted about page
- [ ] Invalid commands show error with help
- [ ] Emojis display correctly
- [ ] Bold text renders properly
- [ ] Check logs for channel detection (should show "whatsapp")

---

## Configuration

### Environment Variables

```bash
# Enable/disable WhatsApp enhanced formatting
ENABLE_WHATSAPP_FORMATTING=True

# If False, WhatsApp messages will be plain text like SMS
```

### Endpoint Options

The app accepts WhatsApp messages at multiple endpoints:
- `/` - Default (works for both SMS and WhatsApp)
- `/whatsapp` - Dedicated WhatsApp endpoint
- `/message` - Generic message endpoint
- `/sms` - Dedicated SMS endpoint

All endpoints work identically - use whichever you prefer!

---

## Troubleshooting

### Issue: Not receiving messages in WhatsApp

**Solutions**:
1. Verify you joined the sandbox (`join [code]`)
2. Check webhook URL is correct and accessible
3. Ensure webhook method is POST
4. Check app logs for incoming requests
5. Verify app is running and healthy (`/health` endpoint)

### Issue: Messages are plain text, no emojis

**Solutions**:
1. Check `ENABLE_WHATSAPP_FORMATTING=True` in .env
2. Restart your app after changing .env
3. Verify channel detection is working (check logs)
4. Ensure WhatsApp client is up to date

### Issue: "Unable to fetch Bitcoin prices"

**Solutions**:
1. Check internet connectivity from server
2. Verify Blockchain.info API is accessible
3. Check app logs for API errors
4. Try again after a few moments (API might be rate-limited)

### Issue: Webhook errors in Twilio debugger

**Solutions**:
1. Check Twilio Debugger: https://www.twilio.com/console/debugger
2. Verify app returns valid TwiML
3. Check app logs for exceptions
4. Ensure app responds within 10 seconds (Twilio timeout)

### Issue: Can't join sandbox - "Invalid code"

**Solutions**:
1. Use the exact code shown in Twilio console
2. Code format is usually: `join word-word`
3. Check for typos
4. Code is case-sensitive
5. Try generating a new sandbox

### Issue: Production number not approved

**Solutions**:
1. Ensure business verification is complete
2. Provide all required documents
3. Business name must match legal entity
4. May take 1-3 weeks - be patient
5. Contact Twilio support if delayed

---

## WhatsApp vs SMS Comparison

| Feature | WhatsApp | SMS |
|---------|----------|-----|
| **Cost to user** | Free (uses data) | Carrier charges |
| **Message length** | 4096 characters | 160 characters (splits after) |
| **Formatting** | Rich (bold, emoji) | Plain text |
| **Media** | Images, docs, audio | Limited (MMS) |
| **Read receipts** | Yes | No |
| **Delivery status** | Yes | Limited |
| **Global reach** | 2B+ users | Universal |
| **Twilio cost** | $0.005-0.03/conversation | $0.0075/message |
| **Setup complexity** | Medium (needs approval) | Easy |

---

## Advanced Features (Future)

Possible enhancements for WhatsApp:

### Interactive Buttons
```python
# Quick reply buttons for currency selection
msg.add_button("USD 🇺🇸", "usd")
msg.add_button("EUR 🇪🇺", "eur")
msg.add_button("GBP 🇬🇧", "gbp")
```

### Rich Media
- Send price charts as images
- PDF receipts for conversions
- Voice messages with prices

### Lists
- Interactive currency picker
- Command menu
- Recent conversions history

### Message Templates
- Price alerts
- Daily summaries
- Weekly reports

---

## Best Practices

### 1. Opt-In Required
- Users must initiate conversation
- Clear opt-out instructions
- Respect 24-hour messaging window

### 2. Clear Communication
- Use formatting wisely (not excessive)
- Keep messages concise
- Provide helpful error messages

### 3. Compliance
- Follow WhatsApp Business Policy
- No spam or promotional content
- Provide value to users
- Quick response times

### 4. Monitoring
- Track message volumes
- Monitor error rates
- Check delivery status
- Log user feedback

---

## Resources

### Official Documentation
- [Twilio WhatsApp API Docs](https://www.twilio.com/docs/whatsapp)
- [WhatsApp Business Policy](https://www.whatsapp.com/legal/business-policy)
- [Twilio WhatsApp Sandbox](https://www.twilio.com/docs/whatsapp/sandbox)

### Helpful Links
- [WhatsApp Formatting Guide](https://faq.whatsapp.com/general/chats/how-to-format-your-messages)
- [Twilio Debugger](https://www.twilio.com/console/debugger)
- [Twilio Console](https://console.twilio.com)

### SMSBtc Resources
- [Main README](README.md)
- [Deployment Guide](DEPLOYMENT.md)
- [GitHub Issues](https://github.com/richvincent/smsbtc/issues)

---

## Getting Help

If you encounter issues:

1. **Check logs** - Look for errors in your app logs
2. **Twilio Debugger** - Check for webhook errors
3. **Test locally** - Use ngrok to test locally
4. **GitHub Issues** - Report bugs or ask questions
5. **Twilio Support** - For WhatsApp approval issues

---

**Ready to connect the unbanked to Bitcoin via WhatsApp!** 🚀
