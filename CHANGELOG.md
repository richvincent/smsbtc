# Changelog

## [2.1.0] - 2025-11-09

### WhatsApp Integration - Multi-Channel Support

This release adds full WhatsApp Business API support alongside SMS, with enhanced formatting and automatic channel detection.

### Added

#### WhatsApp Support
- **Full WhatsApp Business API integration** via Twilio
- **Automatic channel detection** - App automatically detects SMS vs WhatsApp
- **WhatsApp-enhanced formatting**:
  - Emojis for visual appeal (₿, 💰, 📊, 💱, etc.)
  - Country flag emojis for 20+ currencies (🇺🇸, 🇪🇺, 🇬🇧, etc.)
  - Bold text for important information
  - Better message layout with headers and sections
  - Improved readability
- **Backward compatible** - SMS users still get plain text (no emojis)
- **Dual-channel support** - Both SMS and WhatsApp work simultaneously

#### New Files
- `WHATSAPP_SETUP.md` - Comprehensive WhatsApp integration guide
  - Sandbox setup (instant testing)
  - Production setup instructions
  - Troubleshooting guide
  - Feature comparison
  - Best practices

#### New Functions (`run.py`)
- `detect_channel()` - Automatically detects message source (SMS/WhatsApp)
- `get_currency_emoji()` - Maps currencies to country flag emojis
- `format_message()` - Applies channel-specific formatting
- Updated `get_help_message()` - Now accepts channel parameter for custom formatting
- Updated `get_about_message()` - Now accepts channel parameter

#### New Endpoints
- `/whatsapp` - Dedicated WhatsApp webhook endpoint
- `/message` - Generic message endpoint (handles both)
- `/sms` - Dedicated SMS endpoint
- All endpoints support both SMS and WhatsApp automatically

#### New Configuration
- `ENABLE_WHATSAPP_FORMATTING` - Environment variable to toggle rich formatting
  - Default: `True`
  - When `False`, WhatsApp messages use plain text like SMS

### Changed

#### Updated Files
- **run.py** - Complete multi-channel refactor
  - Renamed `sms()` → `handle_message()` for clarity
  - Added channel detection logic
  - Conditional formatting based on channel
  - Enhanced error messages (channel-specific)
  - Improved logging (includes channel info)

- **README.md** - Updated with WhatsApp information
  - Title now includes "SMS & WhatsApp"
  - New Features section with WhatsApp highlights
  - WhatsApp Setup section added
  - WhatsApp vs SMS comparison table
  - Updated Architecture section
  - Updated API Endpoints section
  - Updated Mission statement

- **DEPLOYMENT.md**
  - Added WhatsApp testing to post-deployment checklist
  - Separate SMS and WhatsApp test checklists
  - Reference to WHATSAPP_SETUP.md

- **.env.example**
  - Added `ENABLE_WHATSAPP_FORMATTING=True`

- **/health endpoint** - Now returns channel information
  - Returns both "sms" and "whatsapp" in channels array
  - Version updated to 2.1.0

### Enhanced

#### User Experience (WhatsApp)
- **Price checks** - Beautifully formatted with emojis and bold text
- **Conversions** - Visual currency indicators with flags
- **Help menu** - Organized with emoji icons
- **About page** - Professional formatting with sections
- **Error messages** - Clearer, more helpful error responses
- **Welcome message** - Friendly greeting for first-time users

#### User Experience (SMS)
- **No changes** - SMS users get same plain text experience
- **Full feature parity** - All commands work identically on both channels

### Technical Improvements

- **Zero breaking changes** - Fully backward compatible
- **Single codebase** - Both channels handled by same code
- **Automatic routing** - No manual channel selection needed
- **Environment-based config** - Easy to enable/disable WhatsApp formatting
- **Consistent logging** - Channel info included in all log messages

### Example Comparisons

#### WhatsApp Response ($btcprice usd)
```
*Bitcoin Price* ₿ 🇺🇸

1 BTC = *94,567.00 USD*

💰 Spot price (with 12.5% markup):
*106,387.88 USD*
```

#### SMS Response ($btcprice usd)
```
1 BTC = 94,567.00 USD
Spot price (with 12.5% markup): 106,387.88 USD
```

### Documentation

- **WHATSAPP_SETUP.md** - 400+ lines of comprehensive setup guide
- **README.md** - Updated with WhatsApp sections
- **DEPLOYMENT.md** - WhatsApp testing checklist
- **This CHANGELOG** - Complete feature documentation

### Future WhatsApp Enhancements

Possible future additions:
- [ ] Interactive buttons for currency selection
- [ ] Quick reply buttons
- [ ] Rich media (charts as images)
- [ ] Message templates for alerts
- [ ] Interactive lists
- [ ] PDF receipts

---

## [2.0.0] - 2025-11-09

### Major Update - Modernization & Best Practices

This release brings the project up to modern standards with updated dependencies, improved code quality, and comprehensive documentation.

### Added

#### New Files
- `bitcoin_api.py` - Dedicated module for Bitcoin price API operations
  - Clean separation of concerns
  - Proper error handling with custom exceptions
  - Type hints for better code clarity
  - Replaces deprecated `blockchain` library

- `.env.example` - Environment variable template
  - PORT configuration
  - DEBUG mode setting
  - MARKUP_PERCENTAGE configuration
  - Ready for expansion with Twilio credentials

- `DEPLOYMENT.md` - Comprehensive deployment guide
  - Instructions for 6 hosting platforms (Heroku, Railway, Render, DigitalOcean, AWS EB, Google Cloud Run)
  - Local development setup with ngrok
  - Troubleshooting guide
  - Cost comparison
  - Security best practices

- `CHANGELOG.md` - This file, tracking all changes

- `/health` endpoint - Health check for monitoring

### Changed

#### Dependencies (`requirements.txt`)
- **Flask**: `0.11.1` → `3.1.0` (8+ years of updates!)
- **Werkzeug**: `0.11.11` → `3.1.3`
- **Twilio**: `5.6.0` → `9.3.7` (major API changes)
- **Removed**: `blockchain==1.3.3` (deprecated library)
- **Added**: `requests==2.32.3` (for API calls)
- **Added**: `python-dotenv==1.0.1` (environment variable management)
- **Added**: `gunicorn==23.0.0` (production WSGI server)

#### Python Version (`runtime.txt`)
- **Python**: `3.5.2` → `3.12.7` (7 years newer!)

#### Application Code (`run.py`)
- Complete rewrite with modern Python practices
- Updated Twilio API: `twilio.twiml.Response()` → `MessagingResponse()`
- Added comprehensive logging with Python's `logging` module
- Environment variable support via `python-dotenv`
- Improved error handling with try/except blocks
- Better code organization:
  - Extracted message templates to functions
  - Separated business logic
  - Added docstrings
  - Type hints on functions
- Configurable markup percentage via environment variable
- Case-insensitive command parsing (`$help` == `$HELP`)
- Better error messages for users
- Health check endpoint at `/health`
- Improved currency formatting (thousands separators)
- Better Bitcoin precision (8 decimal places)

#### README (`README.md`)
- Complete rewrite with modern markdown
- Added badges (Python version, Flask version, License)
- Comprehensive table of contents
- Quick start guide with step-by-step instructions
- Command reference table
- Local development instructions
- Multiple deployment options
- Project structure documentation
- ngrok setup for local testing
- Future enhancements section
- Resources and references

#### Configuration
- **Procfile**: Updated to use `gunicorn` instead of direct Python execution
  - Old: `web: python run.py`
  - New: `web: gunicorn run:app --log-file -`

- **.gitignore**: Modernized for current Python ecosystem
  - Added `.env` files
  - Added virtual environment patterns
  - Added IDE-specific files (.vscode, .idea)
  - Added OS-specific files (.DS_Store)
  - Modern Python packaging patterns
  - Testing and coverage directories

### Improved

#### Code Quality
- Added type hints where appropriate
- Proper Python docstrings
- Separated concerns (API logic in separate module)
- Consistent error handling
- Logging for debugging and monitoring
- Better variable naming
- PEP 8 compliance

#### Security
- Environment variable support (no hardcoded secrets)
- Input validation and sanitization
- Proper exception handling (no stack trace exposure)
- Updated dependencies (security patches)
- .env excluded from git

#### User Experience
- Better error messages
- More informative responses
- Clearer command formatting examples
- Support for uppercase/lowercase commands
- Professional number formatting

#### Developer Experience
- Comprehensive documentation
- Multiple deployment options
- Local development guide
- Health check endpoint for monitoring
- Easy configuration via .env
- Better project structure

### Fixed
- Deprecated Twilio API calls
- Outdated dependency versions
- Missing error handling
- No logging capability
- Hardcoded configuration values
- Missing environment variable support

### Deprecated
- Old `blockchain` Python library (replaced with direct API calls)
- Python 3.5 support (now requires 3.10+)

### Removed
- `README.txt` (consolidated into README.md)
- Dependency on deprecated `blockchain` package

### Security
- All dependencies updated to latest stable versions
- Removed known vulnerabilities in old Flask/Werkzeug versions
- Environment variable support prevents credential leaks
- Input validation prevents injection attacks

---

## [1.0.0] - 2016-10-15

### Initial Release
- SMS interface for Bitcoin price information
- Support for multiple currencies via Blockchain.info
- Commands: $btcprice, $currencyconvert, $btcconvert, $listcurrencies, $help, $about
- Flask web application
- Twilio SMS integration
- Heroku deployment support

---

## Migration Guide (1.0 → 2.0)

If you have an existing deployment, follow these steps:

1. **Backup your current deployment**
   ```bash
   git tag v1.0-backup
   ```

2. **Pull latest changes**
   ```bash
   git pull origin main
   ```

3. **Update Python version**
   - Update your hosting platform to use Python 3.12
   - Or modify `runtime.txt` to your preferred version (3.10+ required)

4. **Install new dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file** (optional, for custom configuration)
   ```bash
   cp .env.example .env
   # Edit .env as needed
   ```

6. **Test locally**
   ```bash
   python run.py
   # Visit http://localhost:5000/health
   ```

7. **Deploy**
   ```bash
   git push heroku main  # or your hosting platform
   ```

8. **Verify**
   - Send test SMS to your Twilio number
   - Check `/health` endpoint
   - Monitor logs for any errors

---

## Breaking Changes

### For Developers
- **Python 3.10+ required** (was 3.5)
- **Twilio API updated** - if you customized Twilio code, update to `MessagingResponse`
- **blockchain library removed** - if you used it directly, use `bitcoin_api.py` instead

### For Users
No breaking changes - all SMS commands work identically!

---

## Notes
- The project maintains backward compatibility for end users (SMS interface unchanged)
- All original functionality preserved
- Additional features can be enabled via environment variables
- Production-ready with proper logging and error handling
