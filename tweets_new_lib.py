from bs4 import BeautifulSoup
import requests
import csv

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


# Set the URL of the Twitter search results
url = "https://twitter.com/search?q=%23BlackLivesMatter%20since%3A2020-05-30%20until%3A2020-06-02&src=typed_query"

# Send a GET request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the tweets and extract their timestamp and ID
tweets = soup.find_all("div", class_="tweet")
tweet_data = []
for tweet in tweets:
    timestamp = tweet.find("a", class_="tweet-timestamp")["title"]
    text = tweet.find('p', {'class': 'tweet-text'}).text
    analyzed_text = text_analysis(text)
    tweet_data.append([timestamp, analyzed_text.mood, analyzed_text.score])

# Write the tweet data to a CSV file
with open("tweets00002.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "text_mood", "text_mood_score"])
    writer.writerows(tweet_data)
