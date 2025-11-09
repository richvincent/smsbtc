# SMSBtc Deployment Guide

This guide covers deploying SMSBtc to various hosting platforms.

## Table of Contents

- [Heroku](#heroku)
- [Railway](#railway)
- [Render](#render)
- [DigitalOcean App Platform](#digitalocean-app-platform)
- [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
- [Google Cloud Run](#google-cloud-run)

---

## Heroku

Heroku offers easy deployment with Git integration. Free tier is no longer available, but paid plans start at $5/month.

### Prerequisites
- Heroku account
- Heroku CLI installed

### Deployment Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku

   # Windows (using chocolatey)
   choco install heroku-cli

   # Or download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create smsbtc-your-name
   ```

4. **Set environment variables (optional)**
   ```bash
   heroku config:set MARKUP_PERCENTAGE=12.5
   heroku config:set DEBUG=False
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Check logs**
   ```bash
   heroku logs --tail
   ```

7. **Get your app URL**
   ```bash
   heroku apps:info
   # Or visit: https://smsbtc-your-name.herokuapp.com
   ```

8. **Configure Twilio webhook** to `https://smsbtc-your-name.herokuapp.com/`

---

## Railway

Railway offers generous free tier with $5/month credit. Modern platform with great developer experience.

### Prerequisites
- Railway account (https://railway.app)
- Railway CLI (optional)

### Deployment Steps (Web UI)

1. **Sign up at Railway**
   - Visit https://railway.app
   - Sign in with GitHub

2. **Create new project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your smsbtc repository

3. **Configure**
   - Railway auto-detects Python
   - No additional configuration needed (uses Procfile)

4. **Set environment variables** (optional)
   - Go to Variables tab
   - Add `MARKUP_PERCENTAGE=12.5`
   - Add `DEBUG=False`

5. **Deploy**
   - Railway deploys automatically on push to main branch

6. **Get URL**
   - Click "Settings" → "Generate Domain"
   - Use this URL for Twilio webhook

### Deployment Steps (CLI)

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# Open in browser
railway open
```

---

## Render

Render offers free tier with automatic SSL and great performance.

### Prerequisites
- Render account (https://render.com)

### Deployment Steps

1. **Create account at Render**
   - Visit https://render.com
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select smsbtc repository

3. **Configure Build Settings**
   - **Name**: `smsbtc`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Plan**: Free (or paid for better performance)

4. **Environment Variables** (optional)
   - Add `MARKUP_PERCENTAGE` = `12.5`
   - Add `DEBUG` = `False`

5. **Deploy**
   - Click "Create Web Service"
   - Render builds and deploys automatically

6. **Get URL**
   - Your app will be at: `https://smsbtc.onrender.com`
   - Configure Twilio webhook with this URL

### Notes
- Free tier apps spin down after inactivity (first SMS may be slow)
- Paid tier ($7/month) keeps app always running

---

## DigitalOcean App Platform

DigitalOcean offers $5/month starter tier with good performance.

### Prerequisites
- DigitalOcean account
- GitHub repository

### Deployment Steps

1. **Create account**
   - Visit https://www.digitalocean.com
   - Create account or sign in

2. **Create App**
   - Go to "Apps" in left sidebar
   - Click "Create App"
   - Choose "GitHub" as source
   - Connect and authorize GitHub
   - Select smsbtc repository

3. **Configure App**
   - **Type**: Web Service
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `gunicorn run:app --bind 0.0.0.0:$PORT`
   - **Port**: 8080 (DigitalOcean default)

4. **Environment Variables**
   - Add `MARKUP_PERCENTAGE` = `12.5`
   - Add `DEBUG` = `False`

5. **Choose Plan**
   - Basic ($5/month) or Pro ($12/month)
   - Click "Launch App"

6. **Get URL**
   - App will be at: `https://smsbtc-xxxxx.ondigitalocean.app`
   - Configure Twilio webhook

---

## AWS Elastic Beanstalk

For AWS users. More complex but integrates with AWS ecosystem.

### Prerequisites
- AWS account
- AWS CLI and EB CLI installed

### Deployment Steps

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB application**
   ```bash
   eb init -p python-3.12 smsbtc
   ```

3. **Create environment**
   ```bash
   eb create smsbtc-env
   ```

4. **Set environment variables**
   ```bash
   eb setenv MARKUP_PERCENTAGE=12.5 DEBUG=False
   ```

5. **Deploy**
   ```bash
   eb deploy
   ```

6. **Get URL**
   ```bash
   eb status
   # URL will be shown in output
   ```

7. **Open app**
   ```bash
   eb open
   ```

8. **Configure Twilio webhook** with the EB URL

### Additional Configuration

Create `.ebextensions/python.config`:

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: run:app
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: /var/app/current
```

---

## Google Cloud Run

Serverless container platform from Google. Pay-per-use pricing.

### Prerequisites
- Google Cloud account
- gcloud CLI installed

### Deployment Steps

1. **Install gcloud CLI**
   ```bash
   # macOS
   brew install --cask google-cloud-sdk

   # Or download from: https://cloud.google.com/sdk/docs/install
   ```

2. **Login and set project**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Create Dockerfile**
   ```dockerfile
   FROM python:3.12-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   ENV PORT=8080
   CMD exec gunicorn --bind :$PORT run:app
   ```

4. **Build and deploy**
   ```bash
   gcloud run deploy smsbtc \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

5. **Get URL**
   - URL will be shown in deployment output
   - Format: `https://smsbtc-xxxxx-uc.a.run.app`

6. **Configure Twilio webhook** with Cloud Run URL

### Notes
- Cloud Run scales to zero (no cost when not in use)
- Charged per request and compute time
- Cold starts may cause first SMS to be slow

---

## Local Testing with ngrok

For testing Twilio webhooks during development:

1. **Install ngrok**
   ```bash
   # macOS
   brew install ngrok

   # Or download from: https://ngrok.com/download
   ```

2. **Create account** at https://ngrok.com (free)

3. **Authenticate**
   ```bash
   ngrok config add-authtoken YOUR_TOKEN
   ```

4. **Run your Flask app**
   ```bash
   python run.py
   ```

5. **Start ngrok tunnel**
   ```bash
   ngrok http 5000
   ```

6. **Copy HTTPS URL** (e.g., `https://abc123.ngrok.io`)

7. **Configure Twilio webhook** with ngrok URL

8. **Test** by sending SMS to your Twilio number

---

## Post-Deployment Checklist

After deploying to any platform:

### General
- [ ] App is running and accessible
- [ ] `/health` endpoint returns 200 OK with both SMS and WhatsApp channels listed
- [ ] Webhook uses HTTPS (required by Twilio)
- [ ] Webhook HTTP method is set to POST
- [ ] Check application logs for errors
- [ ] Monitor API rate limits (Blockchain.info)
- [ ] Set up monitoring/alerting (optional)

### SMS Testing
- [ ] Twilio SMS webhook is configured correctly
- [ ] Test SMS with `$help` command
- [ ] Test each command ($btcprice usd, $currencyconvert 100 eur, $btcconvert 0.01 usd)
- [ ] Verify plain text formatting (no emojis)

### WhatsApp Testing (Optional but Recommended)
- [ ] Join Twilio WhatsApp Sandbox (for testing)
- [ ] WhatsApp webhook configured (same URL as SMS or `/whatsapp`)
- [ ] Test WhatsApp with `$help` command
- [ ] Verify rich formatting (emojis, bold text)
- [ ] Test all commands on WhatsApp
- [ ] Check logs show "whatsapp" channel detection
- [ ] For production: Apply for WhatsApp Business Account (see [WHATSAPP_SETUP.md](WHATSAPP_SETUP.md))

---

## Troubleshooting

### App won't start
- Check logs for errors
- Verify all dependencies installed
- Ensure Python version matches runtime.txt
- Check PORT environment variable

### Twilio not receiving responses
- Verify webhook URL is correct and accessible
- Check HTTPS is enabled (HTTP won't work)
- Verify POST method is selected
- Check application logs for incoming requests

### API errors
- Blockchain.info may be rate-limited
- Check internet connectivity from server
- Verify API is not blocked by firewall

### Slow responses
- Free tiers may have cold starts
- Consider upgrading to paid tier
- Check API response times in logs

---

## Monitoring

### Health Check
```bash
curl https://your-app-url.com/health
# Should return: {"status": "healthy", "service": "smsbtc"}
```

### Log Monitoring

**Heroku**:
```bash
heroku logs --tail
```

**Railway**:
```bash
railway logs
```

**Render**: Check Logs tab in dashboard

**DigitalOcean**: Check Runtime Logs in app settings

---

## Scaling Considerations

For high-volume deployments:

1. **Add Redis caching** for Bitcoin prices (reduce API calls)
2. **Implement rate limiting** per phone number
3. **Use PostgreSQL** for user tracking and analytics
4. **Set up monitoring** (Sentry, DataDog, New Relic)
5. **Add multiple API sources** for redundancy
6. **Enable autoscaling** on cloud platform
7. **Use CDN** for static assets (if any)

---

## Cost Comparison

| Platform | Free Tier | Paid Tier | Notes |
|----------|-----------|-----------|-------|
| Railway | $5/month credit | $5/month per service | Great for hobby projects |
| Render | Yes (with limits) | $7/month | Spins down when inactive |
| Heroku | No | $5/month | Eco dynos available |
| DigitalOcean | No | $5/month | Always-on basic tier |
| Cloud Run | Yes (generous) | Pay per use | Best for variable traffic |
| AWS EB | 12 months free | ~$15/month | Complex but powerful |

---

## Security Best Practices

1. **Never commit `.env` file** (already in .gitignore)
2. **Use environment variables** for all secrets
3. **Enable HTTPS** (all platforms do this by default)
4. **Implement rate limiting** to prevent abuse
5. **Validate all user input** (already implemented)
6. **Keep dependencies updated**: `pip list --outdated`
7. **Monitor logs** for suspicious activity
8. **Use Twilio request validation** (future enhancement)

---

## Questions?

If you encounter issues, check:
- Application logs on your hosting platform
- Twilio debugger: https://www.twilio.com/console/debugger
- GitHub Issues: https://github.com/richvincent/smsbtc/issues

Good luck with your deployment!
