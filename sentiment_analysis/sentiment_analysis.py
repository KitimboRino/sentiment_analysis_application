import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of given text using NLTK's VADER sentiment analyzer.
    
    Args:
        text_to_analyse (str): Text to analyze
        
    Returns:
        dict: Contains sentiment label and score
    """
    try:
        # Download required NLTK data (only needed first time)
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            print("Downloading VADER lexicon...")
            nltk.download('vader_lexicon', quiet=True)
        
        # Create VADER sentiment analyzer
        sia = SentimentIntensityAnalyzer()
        
        # Get sentiment scores
        scores = sia.polarity_scores(text_to_analyse)
        
        # Convert VADER compound score (-1 to 1) to match original API format (0 to 1)
        normalized_score = (scores['compound'] + 1) / 2
        
        # Determine sentiment label with SENTIMENT_ prefix to match Watson API
        if scores['compound'] >= 0.05:
            label = 'SENTIMENT_POSITIVE'
        elif scores['compound'] <= -0.05:
            label = 'SENTIMENT_NEGATIVE'
        else:
            label = 'SENTIMENT_NEUTRAL'
        
        # Create response format matching original API
        formatted_response = {
            'documentSentiment': {
                'label': label,
                'score': normalized_score
            },
            'sentiment_details': {
                'positive': scores['pos'],
                'negative': scores['neg'],
                'neutral': scores['neu'],
                'compound': scores['compound']
            }
        }
        
        # Print full response for debugging
        print("Full API Response:", json.dumps(formatted_response, indent=4))
        
        # Return sentiment data
        return {
            'label': label,
            'score': normalized_score
        }
        
    except Exception as e:
        print(f"Error in sentiment analysis: {str(e)}")
        return {"error": f"Sentiment analysis failed: {str(e)}"}