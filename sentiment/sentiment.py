# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client

def sent(str1):
    client = language.LanguageServiceClient()

    # The text to analyze
    text = str1
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    return ('{}'.format(sentiment.score))

#analyze_sentiment("I really hate C")
