"""
Utility functions for technical indicators and trend analysis.
"""

def moving_average(data, window):
    """
    Calculate the moving average for a given window size.
    
    Args:
        data: List or array of price values
        window: Number of periods for the moving average
    
    Returns:
        The moving average value (float)
    """
    if len(data) < window:
        return None
    return sum(data[-window:]) / window


def trend_detection(short_ma, long_ma):
    """
    Determine market trend based on moving averages.
    
    Args:
        short_ma: Short-term moving average value
        long_ma: Long-term moving average value
    
    Returns:
        str: 'Bullish', 'Bearish', or 'Neutral'
    """
    if short_ma is None or long_ma is None:
        return 'Neutral'
    
    difference = short_ma - long_ma
    threshold = long_ma * 0.01  # 1% threshold for neutral zone
    
    if difference > threshold:
        return 'Bullish'
    elif difference < -threshold:
        return 'Bearish'
    else:
        return 'Neutral'
