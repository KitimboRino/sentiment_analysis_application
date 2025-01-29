import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def sentiment_analyzer(text_to_analyse):
       # Get URL from environment variable
    url = os.getenv('SENTIMENT_API_URL')
    
    # Check if URL is available
    if not url:
        print("Error: SENTIMENT_API_URL not found in environment variables")
        return {"error": "API URL not configured"}

    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    response = requests.post(url, json=myobj, headers=header)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"API Error {response.status_code}: {response.text}")
        return {"error": "API request failed"}

    # Parse the JSON response
    formatted_response = json.loads(response.text)
    
    # Print the full response for debugging
    print("Full API Response:", json.dumps(formatted_response, indent=4))

    # Check if 'documentSentiment' exists in the response
    if 'documentSentiment' not in formatted_response:
        print("Error: 'documentSentiment' key is missing in the response.")
        return {"error": "Invalid API response format"}

    # Extract and return sentiment data
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}
