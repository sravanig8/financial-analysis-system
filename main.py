"""
Multi-Agent Financial Analysis System
Main orchestrator that coordinates all agents to generate a comprehensive stock analysis report.
"""

import sys
import os

# Import all agents
from agents.market_agent import fetch_market_data
from agents.news_agent import get_news_headlines
from agents.sentiment_agent import analyze_sentiment
from agents.analysis_agent import analyze_trends
from agents.report_agent import generate_report


def print_separator():
    """Print a visual separator line."""
    print("-" * 60)


def print_header(text):
    """Print a formatted header."""
    print_separator()
    print(f"  {text}")
    print_separator()
    print()


def print_section(title, content):
    """Print a formatted section."""
    print(f"{title}:")
    print(content)
    print()


def main():
    """
    Main orchestrator function that coordinates all agents.
    """
    print("\n")
    print("=" * 60)
    print("  🚀 MULTI-AGENT FINANCIAL ANALYSIS SYSTEM")
    print("=" * 60)
    print()
    
    # Step 1: Get stock symbol from user
    stock_symbol = input("Enter stock symbol (e.g., AAPL, TSLA, MSFT, INFY): ").strip().upper()
    
    if not stock_symbol:
        print("❌ Error: Please enter a valid stock symbol.")
        return
    
    print(f"\n🔍 Analyzing {stock_symbol}...\n")
    
    # Step 2: Call Market Agent
    print("📊 Fetching market data...")
    market_data = fetch_market_data(stock_symbol)
    
    if market_data.get('error'):
        print(f"❌ Error: {market_data.get('message')}")
        return
    
    current_price = market_data['current_price']
    historical_data = market_data['historical_data']
    print(f"✅ Market data retrieved (Current Price: ${current_price})")
    
    # Step 3: Call News Agent
    print("📰 Fetching news headlines...")
    news_data = get_news_headlines(stock_symbol)
    
    if news_data.get('error'):
        print(f"❌ Error: {news_data.get('message')}")
        return
    
    headlines = news_data['headlines']
    news_source = news_data.get('source', 'Unknown')
    print(f"✅ {len(headlines)} headlines from {news_source}")
    
    # Step 4: Call Sentiment Agent
    print("😊 Analyzing sentiment...")
    sentiment_data = analyze_sentiment(headlines)
    
    if sentiment_data.get('error'):
        print(f"❌ Error: {sentiment_data.get('message')}")
        return
    
    sentiment_label = sentiment_data['sentiment_label']
    sentiment_score = sentiment_data['sentiment_score']
    print(f"✅ Sentiment analyzed: {sentiment_label} ({sentiment_score})")
    
    # Step 5: Call Analysis Agent
    print("📈 Computing technical indicators...")
    analysis_data = analyze_trends(historical_data)
    
    if analysis_data.get('error'):
        print(f"❌ Error: {analysis_data.get('message')}")
        return
    
    trend = analysis_data['trend']
    ma_7 = analysis_data.get('ma_7')
    ma_30 = analysis_data.get('ma_30')
    print(f"✅ Trend analyzed: {trend}")
    
    # Step 6: Call Report Agent (Gemini AI)
    print("🤖 Generating AI-powered report...")
    
    report_input = {
        'symbol': stock_symbol,
        'current_price': current_price,
        'trend': trend,
        'sentiment_label': sentiment_label,
        'sentiment_score': sentiment_score,
        'headlines': headlines
    }
    
    report_data = generate_report(report_input)
    
    if report_data.get('error'):
        print(f"❌ Error: {report_data.get('message')}")
        print("\n⚠️  Tip: Make sure you have set the GEMINI_API_KEY environment variable.")
        print("    You can get a free API key from: https://makersuite.google.com/app/apikey")
        return
    
    print("✅ AI report generated")
    print()
    
    # Step 7: Display comprehensive report
    print_header(f"FINANCIAL ANALYSIS REPORT: {stock_symbol}")
    
    # Basic Information
    print_section("Current Price", f"${current_price}")
    print_section("Trend", trend)
    
    # Technical Indicators
    if ma_7 and ma_30:
        print_section("Technical Indicators", 
                     f"  • 7-Day Moving Average: ${ma_7}\n" +
                     f"  • 30-Day Moving Average: ${ma_30}\n" +
                     f"  • Price Change (30 days): {analysis_data.get('price_change_percent', 'N/A')}%")
    
    # Sentiment Analysis
    print_section("Sentiment Analysis", 
                 f"{sentiment_label} (Score: {sentiment_score})")
    
    # Top Headlines
    print("Top Headlines:")
    for i, headline in enumerate(headlines[:5], 1):
        print(f"  {i}. {headline}")
    print()
    
    # AI-Generated Insights
    print_section("AI Insights", report_data.get('insights', 'N/A'))
    
    # Recommendation
    print_section("Recommendation", report_data.get('recommendation', 'N/A'))
    
    # Summary
    print_section("Summary", report_data.get('summary', 'N/A'))
    
    print_separator()
    print("✅ Analysis complete!")
    print_separator()
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Analysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
