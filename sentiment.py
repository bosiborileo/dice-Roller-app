import textblob#to import
from textblob import TextBlob
def get_sentiment(text):
    """
    This function takes in a text string and returns the sentiment polarity as a float value ranging from -1 to 1,
    where -1 is a negative sentiment, 0 is a neutral sentiment, and 1 is a positive sentiment.
    """
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    return sentiment_polarity

# Example usage:
text = "I really enjoyed our conversation today!"
sentiment = get_sentiment(text)
if sentiment > 0:
    print("That's great to hear!")
elif sentiment == 0:
    print("Thanks for letting me know.")
else:
    print("I'm sorry to hear that.")



