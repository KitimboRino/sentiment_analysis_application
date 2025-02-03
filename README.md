# Sentiment Analyzer

This project implements a sentiment analysis service using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer. VADER is specifically attuned to sentiments expressed in social media, and it works well on texts from other domains.

## Features

- Sentiment analysis of text input
- Returns both sentiment label (Positive/Negative/Neutral) and confidence scores
- Built using NLTK's VADER sentiment analyzer
- Local processing (no external API calls needed)
- Compatible with both Python scripts and web applications

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install nltk python-dotenv flask
```

## Usage

The sentiment analyzer can be used in two ways:

### 1. As a Python Function

```python
from sentiment_analyzer import sentiment_analyzer

result = sentiment_analyzer("Your text here")
print(result)
```

### 2. As a Web Service

The analyzer is exposed as a web service endpoint:
```
GET /sentimentAnalyzer?textToAnalyze=your text here
```

## Response Format

The analyzer returns a JSON object with the following structure:
```json
{
    "documentSentiment": {
        "label": "SENTIMENT_POSITIVE",
        "score": 0.81845
    },
    "sentiment_details": {
        "positive": 0.808,
        "negative": 0.0,
        "neutral": 0.192,
        "compound": 0.6369
    }
}
```

Where:
- `label`: The sentiment classification (SENTIMENT_POSITIVE, SENTIMENT_NEGATIVE, or SENTIMENT_NEUTRAL)
- `score`: A normalized score between 0 and 1
- `sentiment_details`: Additional VADER sentiment metrics

## How It Works

The analyzer uses NLTK's VADER sentiment analyzer, which:
1. Takes into account both the polarity and intensity of emotions
2. Handles punctuation, capitalization, and emoticons
3. Is specifically attuned to social media text
4. Works well on short texts as well as longer documents

## Error Handling

The service includes comprehensive error handling:
- Returns error messages if text analysis fails
- Validates input parameters
- Handles missing or malformed input gracefully

## Dependencies

- NLTK: For the VADER sentiment analyzer
- Flask: For the web service
- python-dotenv: For environment variable management