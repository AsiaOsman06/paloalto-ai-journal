from textblob import TextBlob

def analyze_text(text: str):
    blob = TextBlob(text)
    return {
        "sentiment": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }
