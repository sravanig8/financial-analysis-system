"""
News Agent
Fetches real news headlines related to a stock symbol using GNEWS API.
Falls back to generated sandbox headlines if API is unavailable.
"""

import os
import requests
import random


def fetch_real_news_gnews(symbol, company_name=None):
    """
    Fetch real news headlines from GNEWS API.
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'TSLA')
        company_name: Optional company name for better search
    
    Returns:
        list: List of real news headlines or empty list if API fails
    """
    try:
        # Get API key from Streamlit secrets or environment variable
        api_key = None
        try:
            import streamlit as st
            api_key = st.secrets.get("GNEWS_API_KEY")
        except:
            pass
        
        if not api_key:
            api_key = os.environ.get('GNEWS_API_KEY')
        
        if not api_key:
            return []
        
        # Map symbols to company names for better search
        company_map = {
            'AAPL': 'Apple Inc',
            'TSLA': 'Tesla Inc',
            'GOOGL': 'Alphabet Google',
            'MSFT': 'Microsoft',
            'AMZN': 'Amazon',
            'META': 'Meta Platforms',
            'NVDA': 'NVIDIA',
            'NFLX': 'Netflix',
            'INFY': 'Infosys',
            'TCS': 'Tata Consultancy'
        }
        
        company = company_name or company_map.get(symbol.upper(), symbol.upper())
        
        # GNEWS API endpoint
        url = "https://gnews.io/api/v4/search"
        params = {
            'q': f'{company} {symbol}',
            'token': api_key,
            'lang': 'en',
            'max': 10,
            'sortby': 'publishedAt'
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            # Extract headlines
            headlines = [article.get('title', '') for article in articles if article.get('title')]
            return headlines[:8]  # Return up to 8 headlines
        
        return []
    
    except Exception as e:
        print(f"Warning: GNEWS API error: {str(e)}")
        return []


def generate_sample_headlines(symbol, company_name=None):
    """
    Generate sample news headlines as fallback when API is unavailable.
    
    Args:
        symbol: Stock ticker symbol
        company_name: Optional company name
    
    Returns:
        list: List of sample headlines
    """
    # Map common symbols to company names
    company_map = {
        'AAPL': 'Apple',
        'TSLA': 'Tesla',
        'GOOGL': 'Google',
        'MSFT': 'Microsoft',
        'AMZN': 'Amazon',
        'META': 'Meta',
        'NVDA': 'NVIDIA',
        'NFLX': 'Netflix',
        'INFY': 'Infosys',
        'TCS': 'Tata Consultancy Services'
    }
    
    company = company_name or company_map.get(symbol.upper(), symbol.upper())
    
    # Sample headline templates
    positive_headlines = [
        f"{company} stock rises after strong quarterly earnings report",
        f"{company} announces breakthrough innovation, shares gain momentum",
        f"Analysts upgrade {company} stock with positive outlook",
        f"{company} expands market presence with strategic partnership",
        f"Investors bullish on {company} as revenue exceeds expectations"
    ]
    
    neutral_headlines = [
        f"{company} releases quarterly financial results",
        f"{company} CEO discusses company strategy in investor call",
        f"Market analysts review {company} performance amid sector trends",
        f"{company} maintains steady position in competitive market"
    ]
    
    negative_headlines = [
        f"{company} faces headwinds as market conditions tighten",
        f"Concerns grow over {company} profit margins",
        f"{company} stock experiences volatility amid market uncertainty",
        f"Regulatory challenges impact {company} growth prospects"
    ]
    
    # Combine all headlines
    all_headlines = positive_headlines + neutral_headlines + negative_headlines
    num_headlines = random.randint(5, 8)
    return random.sample(all_headlines, min(num_headlines, len(all_headlines)))


def get_news_headlines(symbol, company_name=None):
    """
    Get news headlines - tries real API first, then falls back to samples.
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'TSLA')
        company_name: Optional company name for better headlines
    
    Returns:
        dict: Contains 'headlines' list, 'source' type, and 'error' status
    """
    try:
        # Try to fetch real news from GNEWS API
        real_headlines = fetch_real_news_gnews(symbol, company_name)
        
        if real_headlines and len(real_headlines) > 0:
            return {
                'error': False,
                'headlines': real_headlines,
                'symbol': symbol.upper(),
                'source': 'GNEWS API'
            }
        
        # Fallback to generated sandbox headlines
        sample_headlines = generate_sample_headlines(symbol, company_name)
        return {
            'error': False,
            'headlines': sample_headlines,
            'symbol': symbol.upper(),
            'source': 'Sample (API unavailable)'
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Error fetching headlines: {str(e)}'
        }


if __name__ == '__main__':
    # Test the agent
    result = get_news_headlines('TSLA')
    print(result)


def get_news(symbol):
    """
    Simplified wrapper for fetching news headlines (for Streamlit interface).
    
    Args:
        symbol: Stock ticker symbol
    
    Returns:
        list: List of news headlines or empty list if error
    """
    data = get_news_headlines(symbol)
    if data.get('error'):
        return []
    return data.get('headlines', [])
