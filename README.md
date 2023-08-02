Sentiment analysis is a Natural Language Processing (NLP) task that involves determining the sentiment or emotion expressed in a piece of text. We'll use Python and the nltk library (Natural Language Toolkit) for this task.

This code uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon from the nltk.sentiment.vader module. VADER is a rule-based sentiment analysis tool that performs well for social media text and informal language.

In the analyze_sentiment function, we calculate the sentiment score using the SentimentIntensityAnalyzer from VADER. The score ranges from -1.0 to 1.0, where values close to -1.0 indicate negative sentiment, values close to 1.0 indicate positive sentiment, and values close to 0.0 indicate a neutral sentiment.

Finally, we test the sentiment analysis function with a sample text and print the sentiment category based on the sentiment score.
