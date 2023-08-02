import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

###########################################################################

def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)['compound']
    return sentiment_score

###########################################################################

sample_text = "{YOUR_STATEMENT}"
sentiment_score = analyze_sentiment(sample_text)

###########################################################################

if sentiment_score >= 0.05:
    print("Positive sentiment")
elif sentiment_score <= -0.05:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
