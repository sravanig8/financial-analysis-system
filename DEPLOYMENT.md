# 🚀 Deployment Guide - Streamlit Community Cloud

This guide will help you deploy your Multi-Agent Financial Analysis System to Streamlit Community Cloud for free.

## Prerequisites

- ✅ GitHub account with your code repository
- ✅ Gemini API key (get from https://aistudio.google.com/app/apikeys)
- ✅ GNEWS API key (optional - get from https://gnews.io)

## Step 1: Prepare Your Repository

Your repository is already prepared with all necessary files:
- ✅ `requirements.txt` - Dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `.streamlit/secrets.toml.example` - Secrets template
- ✅ `.gitignore` - Properly configured

## Step 2: Deploy to Streamlit Cloud

### 2.1 Sign Up for Streamlit Cloud

1. Go to **https://streamlit.io/cloud**
2. Click **"Sign up"** or **"Get started"**
3. Sign in with your **GitHub account**
4. Authorize Streamlit to access your repositories

### 2.2 Create a New App

1. Click **"New app"** button
2. Fill in the deployment details:
   - **Repository**: `sravanig8/financial-analysis-system`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: Choose a custom name (e.g., `financial-analysis-ai`)

3. Click **"Advanced settings"** (optional):
   - Python version: `3.10` or higher

### 2.3 Configure Secrets

**IMPORTANT:** You must add your API keys as secrets before the app will work.

1. In the Streamlit Cloud dashboard, click on your app
2. Click the **three dots menu** (⋮) → **"Settings"**
3. Go to the **"Secrets"** tab
4. Add your API keys in TOML format:

```toml
GEMINI_API_KEY = "your-actual-gemini-api-key-here"
GNEWS_API_KEY = "your-actual-gnews-api-key-here"
```

5. Click **"Save"**

> **Note:** Replace the placeholder text with your actual API keys. Do NOT use quotes inside quotes.

### 2.4 Deploy

1. Click **"Deploy!"**
2. Wait 2-3 minutes for the deployment to complete
3. Your app will be live at: `https://your-app-name.streamlit.app`

## Step 3: Test Your Deployment

1. Visit your deployed app URL
2. Check the **System Status** sidebar:
   - ✅ Gemini API: Ready
   - ✅ GNEWS API: Ready (if configured)
3. Enter a stock symbol (e.g., `AAPL`)
4. Click **"🔍 Run Analysis"**
5. Verify all features work:
   - Market data loads
   - Headlines appear
   - Sentiment analysis works
   - AI insights generate successfully

## Troubleshooting

### Issue: "GEMINI_API_KEY not set"

**Solution:**
1. Go to app **Settings** → **Secrets**
2. Ensure you've added:
   ```toml
   GEMINI_API_KEY = "your-key-here"
   ```
3. Click **"Save"** and wait for app to restart

### Issue: App Shows Errors on Launch

**Solution:**
1. Check the **Logs** in Streamlit Cloud dashboard
2. Verify all dependencies in `requirements.txt` are installable
3. Make sure Python version is 3.10+

### Issue: "No module named 'streamlit'"

**Solution:**
- This shouldn't happen, but if it does:
  1. Check `requirements.txt` includes `streamlit`
  2. Redeploy the app

### Issue: API Rate Limit Exceeded

**Solution:**
- Gemini free tier has limited requests
- Wait a few minutes between analyses
- Consider upgrading to paid tier if needed

## Managing Your Deployment

### Update Your Deployment

When you push changes to GitHub:
1. Streamlit Cloud automatically detects changes
2. App redeploys automatically (within 1-2 minutes)
3. No manual action needed!

### Reboot Your App

If the app gets stuck:
1. Go to Streamlit Cloud dashboard
2. Click app menu (⋮) → **"Reboot"**

### Delete/Pause Your App

1. Go to Streamlit Cloud dashboard
2. Click app menu (⋮) → **"Delete"** or **"Pause"**

## Custom Domain (Optional)

Streamlit Cloud apps use URLs like `your-app.streamlit.app`. For a custom domain:

1. Upgrade to Streamlit Cloud Teams (paid)
2. Or use a reverse proxy (advanced)

## Security Best Practices

### ✅ Do's:
- ✅ Always use Streamlit Secrets for API keys
- ✅ Never commit `.streamlit/secrets.toml` to GitHub
- ✅ Rotate API keys if they ever get exposed
- ✅ Use `.gitignore` to exclude sensitive files

### ❌ Don'ts:
- ❌ Never hardcode API keys in your code
- ❌ Don't share your `secrets.toml` file
- ❌ Don't commit `.env` files with real keys

## Cost

- **Streamlit Community Cloud**: 100% FREE
- **Gemini API**: Free tier (generous limits)
- **GNEWS API**: Free tier (limited requests)

**Total Cost: $0** for normal usage!

## Support

- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Gemini API Docs**: https://ai.google.dev/docs
- **Community**: https://discuss.streamlit.io

## Your Deployed App

Once deployed, share your app:
- **App URL**: https://your-app-name.streamlit.app
- **GitHub Repo**: https://github.com/sravanig8/financial-analysis-system

---

**🎉 Congratulations! Your Multi-Agent Financial Analysis System is now live!**
