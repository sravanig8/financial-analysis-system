# 🚀 Multi-Agent Financial Analysis System with Real-Time Market Intelligence

A sophisticated multi-agent AI system that performs comprehensive stock analysis by coordinating multiple specialized agents to fetch market data, analyze trends, evaluate news sentiment, and generate AI-powered financial reports using Google Gemini.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [API Key Setup](#api-key-setup)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
  - [Web Interface (Streamlit)](#web-interface-streamlit)
- [Project Structure](#project-structure)
- [Agent Descriptions](#agent-descriptions)
- [Sample Output](#sample-output)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

This project demonstrates a **multi-agent architecture** where specialized AI agents work together to analyze stocks. Each agent has a specific responsibility, and they collaborate to produce a comprehensive financial analysis report.

**Core Technologies:**
- **Python 3.10+**
- **Google Gemini API** (gemini-pro) for AI-generated insights
- **yfinance** for real-time market data
- **TextBlob** for sentiment analysis
- **pandas & numpy** for data processing

## ✨ Features

- ✅ **Real-time stock data** fetching via yfinance
- ✅ **Technical analysis** with moving averages and trend detection
- ✅ **Real news headlines** from GNEWS API or generated samples
- ✅ **Sentiment analysis** using natural language processing
- ✅ **AI-powered report generation** using Google Gemini
- ✅ **Multi-agent coordination** for comprehensive analysis
- ✅ **Command-line interface** for power users
- ✅ **Web interface (Streamlit)** for browser-based analysis
- ✅ **Free tools only** - no paid APIs required (Gemini has a free tier)

## 🏗️ Architecture

The system uses a **multi-agent orchestration pattern** where each agent is an independent module with a specific task:

```
┌─────────────────────────────────────────────────────────────┐
│                      Main Orchestrator                       │
│                         (main.py)                            │
└──────────────┬──────────────────────────────────────────────┘
               │
               ├──► Market Agent ──────► Fetch stock prices & history
               │
               ├──► News Agent ────────► Generate news headlines
               │
               ├──► Sentiment Agent ───► Analyze headline sentiment
               │
               ├──► Analysis Agent ────► Compute technical indicators
               │
               └──► Report Agent ──────► Generate AI insights (Gemini)
                                          
                    ▼
           Final Comprehensive Report
```

### Agent Workflow:

1. **User Input**: Stock symbol (e.g., AAPL, TSLA)
2. **Market Agent**: Fetches current price and 30-day historical data
3. **News Agent**: Generates relevant news headlines
4. **Sentiment Agent**: Analyzes sentiment of headlines (positive/neutral/negative)
5. **Analysis Agent**: Computes moving averages and trend direction
6. **Report Agent**: Uses Gemini AI to generate professional insights and recommendations
7. **Output**: Comprehensive formatted report in the terminal

## 💻 System Requirements

- **Python**: 3.10 or higher
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for fetching stock data and AI generation
- **Gemini API Key**: Free API key from Google

## 📦 Installation

### Step 1: Clone or Download the Project

If you haven't already, navigate to your project directory:

```bash
cd c:\Users\hp\finance
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `google-genai` - Google Gemini API client (latest version)
- `yfinance` - Yahoo Finance market data
- `textblob` - Sentiment analysis
- `pandas` - Data manipulation
- `numpy` - Numerical operations

### Step 4: Download TextBlob Corpora (One-time Setup)

After installing TextBlob, download required data:

```bash
python -m textblob.download_corpora
```

## 🔑 API Key Setup

### Get Your Free Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key

### Set the Environment Variable

#### On Windows (PowerShell):

```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

To make it permanent:
```powershell
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-api-key-here', 'User')
```

#### On macOS/Linux (Bash):

```bash
export GEMINI_API_KEY="your-api-key-here"
```

To make it permanent, add to `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Optional: Set GNEWS API Key for Real Headlines

To use **real news headlines** instead of generated samples:

1. Go to [GNEWS](https://gnews.io)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Set the environment variable:

#### On Windows (PowerShell):

```powershell
$env:GNEWS_API_KEY="your-gnews-api-key-here"
```

#### On macOS/Linux (Bash):

```bash
export GNEWS_API_KEY="your-gnews-api-key-here"
```

**Note**: If `GNEWS_API_KEY` is not set, the system automatically uses generated sample headlines.

## 🚀 Usage

### Command-Line Interface

```bash
python main.py
```

Then follow the prompts:

```
Enter stock symbol (e.g., AAPL, TSLA, MSFT, INFY): AAPL
```

The system will:
1. Fetch market data
2. Fetch real news headlines (or use samples if GNEWS_API_KEY not set)
3. Analyze sentiment
4. Compute technical indicators
5. Generate AI-powered insights

A comprehensive report will be displayed in your terminal.

### Web Interface (Streamlit)

**Run the web application:**

```bash
streamlit run app.py
```

This will open a web browser automatically with the Streamlit interface at `http://localhost:8501`.

**Using the Web Interface:**

1. Enter a stock symbol in the input field (e.g., AAPL, TSLA, INFY)
2. Click the "🔍 Analyze Stock" button
3. Wait for the analysis to complete
4. View results in different tabs:
   - 📈 **Price & Trend** - Current price and market trend
   - 😊 **Sentiment** - Overall sentiment and individual headline scores
   - 📰 **Headlines** - News headlines used in analysis
   - 🤖 **AI Report** - AI-generated insights and recommendations
   - 📊 **Details** - Detailed analysis data in JSON format

**Features of the Web Interface:**
- 🎨 Clean, intuitive user interface
- 📊 Real-time analysis results
- 🔄 Live status updates during analysis
- 📈 Color-coded indicators (Bullish 🟢, Bearish 🔴, Neutral 🟡)
- 📱 Responsive design works on desktop and tablet
- 💾 Results displayed in easy-to-read format

**Troubleshooting Web Interface:**
- If the page doesn't auto-open, manually go to `http://localhost:8501`
- To stop the server, press `Ctrl+C` in the terminal
- Clear browser cache if you see stale data

## 📁 Project Structure

```
financial-agent/
│
├── main.py                    # Main orchestrator (CLI)
├── app.py                     # Streamlit web interface
│
├── agents/                    # Agent modules
│   ├── market_agent.py       # Fetches market data (yfinance)
│   ├── news_agent.py         # Fetches real news (GNEWS API) or samples
│   ├── sentiment_agent.py    # Analyzes sentiment (TextBlob)
│   ├── analysis_agent.py     # Computes technical indicators
│   └── report_agent.py       # Generates AI report (Gemini)
│
├── utils/                     # Utility functions
│   └── indicators.py         # Moving averages & trend detection
│
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🤖 Agent Descriptions

### 1. Market Agent (`market_agent.py`)

**Responsibility**: Fetch real-time and historical stock data

**Technology**: yfinance API

**Output**:
- Current stock price
- 30-day historical closing prices
- Data validation

### 2. News Agent (`news_agent.py`)

**Responsibility**: Fetch real headlines from GNEWS API or generate samples

**Technology**: GNEWS API (free tier available) + fallback generation

**Features**:
- Fetches real news when `GNEWS_API_KEY` is set
- Automatically falls back to generated samples if API is unavailable
- Up to 8 headlines per analysis

**Output**:
- 5-8 relevant news headlines
- Source indicator (GNEWS API or Sample)
- Company-specific context

### 3. Sentiment Agent (`sentiment_agent.py`)

**Responsibility**: Analyze sentiment of news headlines

**Technology**: TextBlob NLP library

**Output**:
- Sentiment label (Positive/Neutral/Negative)
- Average sentiment score (-1 to +1)
- Individual headline scores

### 4. Analysis Agent (`analysis_agent.py`)

**Responsibility**: Compute technical indicators

**Technology**: Custom algorithms (moving averages)

**Output**:
- 7-day moving average
- 30-day moving average
- Trend direction (Bullish/Bearish/Neutral)
- Price change percentage

### 5. Report Agent (`report_agent.py`)

**Responsibility**: Generate AI-powered insights

**Technology**: Google Gemini API (gemini-pro model)

**Output**:
- Key insights (3-4 bullet points)
- Recommendation (BUY/HOLD/SELL)
- Executive summary

## 📊 Sample Output

```
============================================================
  🚀 MULTI-AGENT FINANCIAL ANALYSIS SYSTEM
============================================================

Enter stock symbol (e.g., AAPL, TSLA, MSFT, INFY): AAPL

🔍 Analyzing AAPL...

📊 Fetching market data...
✅ Market data retrieved (Current Price: $175.50)
📰 Generating news headlines...
✅ 6 headlines generated
😊 Analyzing sentiment...
✅ Sentiment analyzed: Positive (0.28)
📈 Computing technical indicators...
✅ Trend analyzed: Bullish
🤖 Generating AI-powered report...
✅ AI report generated

------------------------------------------------------------
  FINANCIAL ANALYSIS REPORT: AAPL
------------------------------------------------------------

Current Price:
$175.50

Trend:
Bullish

Technical Indicators:
  • 7-Day Moving Average: $174.20
  • 30-Day Moving Average: $170.85
  • Price Change (30 days): 2.72%

Sentiment Analysis:
Positive (Score: 0.28)

Top Headlines:
  1. Apple announces breakthrough innovation, shares gain momentum
  2. Apple stock rises after strong quarterly earnings report
  3. Analysts upgrade Apple stock with positive outlook
  4. Apple expands market presence with strategic partnership
  5. Investors bullish on Apple as revenue exceeds expectations

AI Insights:
[Gemini-generated insights about Apple's market position...]

Recommendation:
BUY: [Gemini-generated recommendation with reasoning...]

Summary:
[Gemini-generated executive summary...]

------------------------------------------------------------
✅ Analysis complete!
------------------------------------------------------------
```

## 🔧 Troubleshooting

### Issue: "GEMINI_API_KEY environment variable not set"

**Solution**: Make sure you've set the API key as described in [API Key Setup](#api-key-setup)

### Issue: "No data found for symbol"

**Solution**: 
- Verify the stock symbol is correct
- Check your internet connection
- Try a well-known symbol like AAPL or MSFT

### Issue: "ModuleNotFoundError"

**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt
```

### Issue: TextBlob errors

**Solution**: Download required corpora
```bash
python -m textblob.download_corpora
```

### Issue: Gemini API rate limit

**Solution**: 
- Free tier has rate limits
- Wait a few minutes between requests
- Consider upgrading if needed

## 🚀 Future Enhancements

Potential improvements for this system:

1. **Real News Integration**: Replace simulated headlines with actual news APIs (NewsAPI, Alpha Vantage)
2. **Portfolio Analysis**: Analyze multiple stocks simultaneously
3. **Historical Backtesting**: Test strategies on historical data
4. **Web Dashboard**: Add Flask/Streamlit interface
5. **Database Storage**: Store analysis results for trend tracking
6. **Email Reports**: Send reports via email
7. **Advanced Indicators**: Add RSI, MACD, Bollinger Bands
8. **PDF Export**: Generate downloadable PDF reports
9. **Real-time Alerts**: Notify on price/sentiment changes
10. **Multi-model AI**: Compare insights from different AI models

## 📝 Notes

- This system is for **educational purposes** and should not be used as sole investment advice
- Market data may have a 15-20 minute delay
- Sentiment analysis is based on headline text and may not reflect actual market sentiment
- Always consult with financial professionals before making investment decisions

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- **Google Gemini** for AI-powered insights
- **Yahoo Finance** for market data
- **TextBlob** for sentiment analysis capabilities

---

**Built with ❤️ using Python and Multi-Agent AI Architecture**
