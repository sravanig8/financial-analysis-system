## Setup Guide for GNEWS API

### How to Get Your GNEWS API Key

1. Visit: https://gnews.io
2. Click "Get API Key" or sign up
3. Create a free account (or use existing one)
4. Go to your dashboard
5. Copy your API key

### Setting Up GNEWS_API_KEY Environment Variable

#### Windows (PowerShell)

**Temporary** (for this session only):
```powershell
$env:GNEWS_API_KEY="your-api-key-here"
```

**Permanent** (for all future sessions):
```powershell
[System.Environment]::SetEnvironmentVariable('GNEWS_API_KEY', 'your-api-key-here', 'User')
```

Then close and reopen PowerShell for the change to take effect.

#### macOS/Linux (Bash)

**Temporary** (for this session only):
```bash
export GNEWS_API_KEY="your-api-key-here"
```

**Permanent** (for all future sessions):
Add to your shell profile (`~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):
```bash
echo 'export GNEWS_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Verify Your Setup

To verify the API key is set correctly:

#### PowerShell:
```powershell
echo $env:GNEWS_API_KEY
```

#### Bash:
```bash
echo $GNEWS_API_KEY
```

### Run the System with Real News

Once your API key is set:

```bash
python main.py
```

Enter a stock symbol and you'll see real news headlines from GNEWS API!

### What Happens if API Key is Not Set?

The system automatically falls back to **generated sample headlines** so it still works perfectly. You'll see:
```
📰 Fetching news headlines...
✅ 5 headlines from Sample (API unavailable)
```

### Features with GNEWS API

- ✅ Real-time news headlines
- ✅ Multiple sources
- ✅ English language filtering
- ✅ Sorted by publish date
- ✅ Automatic fallback to samples if API fails

### Free Tier Limits

GNEWS API free tier includes:
- Limited requests per day (check their website for current limits)
- Full API functionality for development
- Multiple domains support

### Troubleshooting

**Q: Getting "401 Unauthorized" error?**
A: Your API key might be invalid. Double-check it on the GNEWS dashboard.

**Q: No headlines showing?**
A: This is normal - the system falls back to generated samples if API fails.

**Q: Want to verify API works before running main.py?**
A: Test with this command:
```bash
python test_gnews.py
```

Note: You'll need to create test_gnews.py first, or manually test with curl/postman.
