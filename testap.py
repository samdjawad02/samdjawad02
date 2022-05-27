import nltk

nltk.downloader.download('stopwords')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

nltk.download('vader_lexicon')

data = '''
i will kill you

'''
text = data.lower()
sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
print(sentiment)
