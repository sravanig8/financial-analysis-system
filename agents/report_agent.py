"""
Report Agent
Generates AI-powered financial analysis reports using Google Gemini API.
"""

import os
from google import genai
from google.genai import types


def generate_report(stock_data):
    """
    Generate a comprehensive financial report using Gemini AI.
    
    Args:
        stock_data: Dictionary containing all collected data:
            - symbol: Stock ticker
            - current_price: Current stock price
            - trend: Market trend (Bullish/Bearish/Neutral)
            - sentiment_label: Sentiment classification
            - sentiment_score: Numerical sentiment score
            - headlines: List of news headlines
    
    Returns:
        dict: Contains AI-generated report sections and 'error' status
    """
    try:
        # Get API key from Streamlit secrets or environment variable
        api_key = None
        try:
            import streamlit as st
            if "GEMINI_API_KEY" in st.secrets:
                api_key = st.secrets["GEMINI_API_KEY"]
        except:
            pass
        
        if not api_key:
            api_key = os.environ.get('GEMINI_API_KEY')
        
        if not api_key:
            return {
                'error': True,
                'message': 'GEMINI_API_KEY not set. Please configure it in Streamlit secrets or environment variables.'
            }
        
        # Configure Gemini API
        client = genai.Client(api_key=api_key)
        
        # Prepare the prompt for Gemini
        prompt = f"""
You are a professional financial analyst. Based on the following data, provide a comprehensive stock analysis report.

Stock Symbol: {stock_data.get('symbol', 'N/A')}
Current Price: ${stock_data.get('current_price', 'N/A')}
Market Trend: {stock_data.get('trend', 'N/A')}
Sentiment Analysis: {stock_data.get('sentiment_label', 'N/A')} (Score: {stock_data.get('sentiment_score', 'N/A')})

Recent News Headlines:
{chr(10).join([f"- {headline}" for headline in stock_data.get('headlines', [])[:5]])}

Please provide:

1. KEY INSIGHTS (3-4 bullet points analyzing the current market position)

2. RECOMMENDATION (Choose one: BUY, HOLD, or SELL - and explain why in 2-3 sentences)

3. SUMMARY (A concise 3-4 sentence overview of the stock's current state and outlook)

Format your response exactly as follows:

KEY INSIGHTS:
[Your insights here]

RECOMMENDATION:
[BUY/HOLD/SELL]: [Your explanation]

SUMMARY:
[Your summary here]
"""
        
        # Generate content using Gemini
        response = client.models.generate_content(
            model='models/gemini-2.5-flash',
            contents=prompt
        )
        
        # Access the response text
        report_text = response.text if hasattr(response, 'text') else str(response)
        
        if not report_text:
            return {
                'error': True,
                'message': 'Failed to generate report from Gemini API'
            }
        
        # Parse the response
        report_text = report_text.strip()
        
        # Extract sections (simple parsing)
        insights = ""
        recommendation = ""
        summary = ""
        
        sections = report_text.split('\n\n')
        current_section = None
        
        for section in sections:
            section_upper = section.upper()
            if 'KEY INSIGHTS' in section_upper:
                current_section = 'insights'
                insights = section.split(':', 1)[1].strip() if ':' in section else section
            elif 'RECOMMENDATION' in section_upper:
                current_section = 'recommendation'
                recommendation = section.split(':', 1)[1].strip() if ':' in section else section
            elif 'SUMMARY' in section_upper:
                current_section = 'summary'
                summary = section.split(':', 1)[1].strip() if ':' in section else section
            elif current_section == 'insights':
                insights += '\n\n' + section
            elif current_section == 'recommendation':
                recommendation += '\n\n' + section
            elif current_section == 'summary':
                summary += '\n\n' + section
        
        # If parsing fails, return the full text
        if not insights and not recommendation and not summary:
            insights = report_text
            recommendation = "Please review the full analysis above."
            summary = "See detailed analysis for complete insights."
        
        return {
            'error': False,
            'insights': insights.strip(),
            'recommendation': recommendation.strip(),
            'summary': summary.strip(),
            'full_report': report_text
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Error generating report: {str(e)}'
        }


if __name__ == '__main__':
    # Test the agent
    test_data = {
        'symbol': 'AAPL',
        'current_price': 175.50,
        'trend': 'Bullish',
        'sentiment_label': 'Positive',
        'sentiment_score': 0.25,
        'headlines': [
            'Apple announces new product lineup',
            'Apple stock rises on strong earnings',
            'Analysts bullish on Apple future'
        ]
    }
    result = generate_report(test_data)
    print(result)


def generate_financial_report(symbol, price, trend, sentiment_label, sentiment_score, headlines):
    """
    Simplified wrapper for report generation (for Streamlit interface).
    
    Args:
        symbol: Stock ticker symbol
        price: Current stock price
        trend: Market trend (Bullish/Bearish/Neutral)
        sentiment_label: Sentiment classification
        sentiment_score: Numerical sentiment score
        headlines: List of news headlines
    
    Returns:
        dict: Contains 'insights', 'recommendation', 'summary', and 'error' status
    """
    stock_data = {
        'symbol': symbol,
        'current_price': price,
        'trend': trend,
        'sentiment_label': sentiment_label,
        'sentiment_score': sentiment_score,
        'headlines': headlines
    }
    return generate_report(stock_data)
