from nltk.sentiment import SentimentIntensityAnalyzer

def find_sentiment_intensity(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment