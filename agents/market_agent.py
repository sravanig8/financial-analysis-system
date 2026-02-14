"""
Market Data Agent
Fetches real-time and historical stock data using yfinance.
"""

import yfinance as yf


def fetch_market_data(symbol):
    """
    Fetch current price and historical data for a stock symbol.
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'TSLA')
    
    Returns:
        dict: Contains 'current_price', 'historical_data', and 'error' status
    """
    try:
        # Create ticker object
        ticker = yf.Ticker(symbol)
        
        # Fetch historical data for last 30 days
        historical_data = ticker.history(period='1mo')
        
        if historical_data.empty:
            return {
                'error': True,
                'message': f'No data found for symbol {symbol}'
            }
        
        # Get current price (latest close)
        current_price = historical_data['Close'].iloc[-1]
        
        # Extract closing prices as a list
        closing_prices = historical_data['Close'].tolist()
        
        return {
            'error': False,
            'current_price': round(current_price, 2),
            'historical_data': closing_prices,
            'symbol': symbol.upper()
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Error fetching data: {str(e)}'
        }


if __name__ == '__main__':
    # Test the agent
    result = fetch_market_data('AAPL')
    print(result)


def get_market_data(symbol):
    """
    Simplified wrapper for fetching market data (for Streamlit interface).
    
    Args:
        symbol: Stock ticker symbol
    
    Returns:
        tuple: (price, historical_data) or (None, None) if error
    """
    data = fetch_market_data(symbol)
    if data.get('error'):
        return None, None
    return data.get('current_price'), data.get('historical_data')
