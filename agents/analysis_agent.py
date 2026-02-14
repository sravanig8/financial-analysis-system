"""
Analysis Agent
Computes technical indicators and determines market trends.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.indicators import moving_average, trend_detection


def analyze_trends(historical_data):
    """
    Analyze market trends using technical indicators.
    
    Args:
        historical_data: List of historical closing prices
    
    Returns:
        dict: Contains trend analysis results and 'error' status
    """
    try:
        if not historical_data or len(historical_data) < 7:
            return {
                'error': True,
                'message': 'Insufficient historical data for analysis (need at least 7 days)'
            }
        
        # Calculate moving averages
        ma_7 = moving_average(historical_data, 7)   # Short-term (7-day MA)
        ma_30 = moving_average(historical_data, 30) # Long-term (30-day MA)
        
        # Determine trend direction
        trend = trend_detection(ma_7, ma_30)
        
        # Additional metrics
        latest_price = historical_data[-1]
        price_change = ((latest_price - historical_data[0]) / historical_data[0]) * 100
        
        return {
            'error': False,
            'trend': trend,
            'ma_7': round(ma_7, 2) if ma_7 else None,
            'ma_30': round(ma_30, 2) if ma_30 else None,
            'price_change_percent': round(price_change, 2),
            'data_points': len(historical_data)
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Error analyzing trends: {str(e)}'
        }


if __name__ == '__main__':
    # Test the agent
    test_data = [150, 152, 151, 153, 155, 154, 156, 158, 157, 160]
    result = analyze_trends(test_data)
    print(result)


def analyze_trend(historical_data):
    """
    Simplified wrapper for trend analysis (for Streamlit interface).
    
    Args:
        historical_data: List of historical closing prices
    
    Returns:
        tuple: (trend, short_ma, long_ma) or (None, None, None) if error
    """
    data = analyze_trends(historical_data)
    if data.get('error'):
        return None, None, None
    return data.get('trend'), data.get('ma_7'), data.get('ma_30')
