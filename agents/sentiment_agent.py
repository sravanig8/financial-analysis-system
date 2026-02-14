"""
Sentiment Analysis Agent
Analyzes sentiment of news headlines using TextBlob.
"""

from textblob import TextBlob


def analyze_sentiment(headlines):
    """
    Analyze sentiment of news headlines.
    
    Args:
        headlines: List of news headline strings
    
    Returns:
        dict: Contains 'sentiment_label', 'sentiment_score', 'individual_scores', and 'error' status
    """
    try:
        if not headlines:
            return {
                'error': True,
                'message': 'No headlines provided for sentiment analysis'
            }
        
        # Analyze sentiment for each headline
        sentiment_scores = []
        individual_scores = []
        
        for headline in headlines:
            blob = TextBlob(headline)
            polarity = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
            sentiment_scores.append(polarity)
            individual_scores.append({
                'headline': headline,
                'score': round(polarity, 3)
            })
        
        # Calculate average sentiment score
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        
        # Classify sentiment
        if avg_sentiment > 0.1:
            sentiment_label = 'Positive'
        elif avg_sentiment < -0.1:
            sentiment_label = 'Negative'
        else:
            sentiment_label = 'Neutral'
        
        return {
            'error': False,
            'sentiment_label': sentiment_label,
            'sentiment_score': round(avg_sentiment, 3),
            'individual_scores': individual_scores
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Error analyzing sentiment: {str(e)}'
        }


if __name__ == '__main__':
    # Test the agent
    test_headlines = [
        "Apple stock rises after strong earnings",
        "Apple faces supply chain challenges",
        "Analysts neutral on Apple's future outlook"
    ]
    result = analyze_sentiment(test_headlines)
    print(result)