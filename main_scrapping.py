import csv

import snscrape.modules.twitter as sntwitter

from transformers import pipeline


class TextAnalysisResult:
    def __init__(self, mood, score):
        self.mood = mood
        self.score = score


def text_analysis(text_for_analysis):
    # create a sentiment analysis pipeline
    sentiment_analysis = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

    # analyze the sentiment of the text
    result = sentiment_analysis(text_for_analysis)

    return TextAnalysisResult(result[0]['label'], result[0]['score'])


# Configure the search parameters
query = "#BlackLivesMatter since:2020-05-30 until:2020-05-30"

# Search for tweets with the hashtag
# tweets = []
# for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#     tweets.append([tweet.date, tweet.rawContent])

# Save the tweets to a CSV file
with open("tweets31MAY2020.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "mood", "score"])
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        # printing dates to make sure that program works properly and that the tweets are in specified range
        print(tweet.date)
        analysis = text_analysis(tweet.rawContent)
        score = ("{:.2f}".format(analysis.score))
        writer.writerow([tweet.date, analysis.mood, score])
print('done!!!!!!!!!!!!!!!!!!!')