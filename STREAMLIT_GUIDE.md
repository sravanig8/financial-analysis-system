# 🌐 Streamlit Web Interface Quick Start

## What is Streamlit?

Streamlit is a free, open-source framework that turns Python scripts into interactive web applications without requiring HTML, CSS, or JavaScript knowledge.

## Getting Started with the Web Interface

### Prerequisites

Make sure you have:
1. Python 3.10+ installed
2. All dependencies installed from `requirements.txt`
3. `GEMINI_API_KEY` environment variable set
4. (Optional) `GNEWS_API_KEY` environment variable set

### Installation

If Streamlit isn't already installed:

```bash
pip install streamlit
```

### Running the Web Application

Navigate to the project directory and run:

```bash
streamlit run app.py
```

This will:
1. Start a local web server (usually on `http://localhost:8501`)
2. Automatically open the app in your default browser
3. Display a message in the terminal with the URL if it doesn't auto-open

### Using the Interface

1. **Enter Stock Symbol**
   - Type a stock symbol (e.g., AAPL, TSLA, MSFT, INFY)
   - Press Enter or click outside the field

2. **Analyze**
   - Click the blue "🔍 Analyze Stock" button
   - Wait for the analysis to complete (usually 10-30 seconds)

3. **View Results**
   - Results appear automatically in tabs:
     - **📈 Price & Trend** - Displays current price and market trend
     - **😊 Sentiment** - Shows sentiment analysis of news
     - **📰 Headlines** - Lists the headlines analyzed
     - **🤖 AI Report** - AI-generated insights and recommendations
     - **📊 Details** - Raw analysis data in JSON format

### Interface Components

#### Header Section
- Title: "📊 Multi-Agent Financial Analysis System"
- Subtitle explaining the multi-agent architecture

#### Input Section
- Text field for stock symbol
- Primary button to trigger analysis

#### Results Tabs

**Tab 1: Price & Trend**
- Current stock price (large metric)
- Market trend with emoji indicator
- Technical moving averages (7-day and 30-day)

**Tab 2: Sentiment**
- Overall sentiment classification (Positive 🟢, Negative 🔴, Neutral 🟡)
- Numerical sentiment score (-1.0 to +1.0)
- Individual sentiment scores for each headline

**Tab 3: Headlines**
- Up to 8 news headlines
- Numbered list format
- Source: Real headlines from GNEWS API or generated samples

**Tab 4: AI Report**
- **Key Insights**: 3-4 main points about the stock
- **Recommendation**: BUY 🟢, HOLD 🟡, or SELL 🔴
- **Summary**: Executive summary paragraph

**Tab 5: Details**
- Full data in JSON format
- Complete AI-generated report text
- Useful for debugging or detailed analysis

### Sidebar Features

The left sidebar shows:
1. System description (what each agent does)
2. API Key status (configured or not)
3. Helpful information

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Stop the Streamlit server |
| `R` | Rerun the app |
| `C` | Clear cache |

### Troubleshooting

#### Issue: Browser doesn't open automatically
**Solution**: Manually navigate to `http://localhost:8501` in your browser

#### Issue: "No data found for symbol"
**Solution**: Verify the stock symbol is correct. Examples:
- US stocks: AAPL, MSFT, TSLA
- Indian stocks: INFY, RELIANCE.NS, TCS.NS
- Other markets: Follow the market's ticker format

#### Issue: "GEMINI_API_KEY not set"
**Solution**: Set the environment variable before running:

PowerShell:
```powershell
$env:GEMINI_API_KEY="your-api-key"
streamlit run app.py
```

Bash:
```bash
export GEMINI_API_KEY="your-api-key"
streamlit run app.py
```

#### Issue: "Headlines not found"
**Solution**: This is normal. The system uses GNEWS API if available or generates sample headlines. If GNEWS_API_KEY is not set, sample headlines will be used automatically.

#### Issue: Slow analysis
**Solution**: This is normal. Analysis includes:
- Fetching market data from Yahoo Finance (2-5 seconds)
- Fetching news headlines (2-3 seconds)
- Sentiment analysis (1-2 seconds)
- AI report generation via Gemini (5-10 seconds)
- **Total: Usually 15-30 seconds**

### Advanced Usage

#### Run on a specific port
```bash
streamlit run app.py --server.port 8888
```

#### Run in headless mode (don't open browser)
```bash
streamlit run app.py --logger.level=error --client.showErrorDetails=false
```

#### Deploy to the internet
You can deploy this to services like:
- [Streamlit Cloud](https://streamlit.io/cloud) - Free
- [Heroku](https://www.heroku.com/) - Free tier available
- [AWS](https://aws.amazon.com/) - EC2 or App Runner
- [DigitalOcean](https://www.digitalocean.com/) - Droplets

### Performance Tips

1. **For faster analysis**: Set GNEWS_API_KEY to use real headlines instead of generating
2. **For better accuracy**: Analyze well-known stocks (AAPL, MSFT, TSLA, etc.)
3. **API rate limits**: Respect Gemini API rate limits by not running too many analyses quickly

### Support & Feedback

For issues or feature requests:
1. Check the [Streamlit documentation](https://docs.streamlit.io/)
2. Review the `README.md` for system architecture
3. Check API key configuration in the sidebar

---

**Happy analyzing! 📈**
