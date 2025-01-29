from flask import Flask, render_template, request
from sentiment_analysis.sentiment_analysis import sentiment_analyzer
import os

app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)

    if response.get('label') is None:
        return "Invalid input! Try again."
    
    return f"The given text has been identified as {response['label'].split('_')[1]} with a score of {response['score']}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
