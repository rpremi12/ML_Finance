# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
# Instantiates a client
client = language.LanguageServiceClient()
#credentials = service_account.Credentials.from_service_account_file('/path/to/json.json')
# The text to analyze
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))