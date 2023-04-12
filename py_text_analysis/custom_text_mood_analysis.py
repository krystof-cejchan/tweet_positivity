import tweepy
import csv
from transformers import pipeline

# create a sentiment analysis pipeline
sentiment_analysis = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# prompt the user to enter text to analyze
text = input("Enter text to analyze: ")

# analyze the sentiment of the text
result = sentiment_analysis(text)

# output the sentiment analysis result
if result[0]['label'] == 'POSITIVE':
    print(f"The text is positive with a score of {result[0]['score']:.2f}")
elif result[0]['label'] == 'NEGATIVE':
    print(f"The text is negative with a score of {result[0]['score']:.2f}")
else:
    print("Unable to determine the sentiment of the text.")

# Enter your Twitter API credentials here
# consumer_key = "your_consumer_key"
# consumer_secret = "your_consumer_secret"
# access_token = "your_access_token"
# access_token_secret = "your_access_token_secret"
#
# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# # Create API object
# api = tweepy.API(auth)
#
# # The hashtag to search for
# hashtag = "#example"
#
# # Search for tweets containing the hashtag
# tweets = api.search(q=hashtag, count=100)
#
# # Evaluate the sentiment of each tweet
# tweet_sentiments = []
# for tweet in tweets:
#     analysis = TextBlob(tweet.text)
#     sentiment = analysis.sentiment.polarity
#     if sentiment > 0:
#         sentiment_string = "Positive"
#     elif sentiment == 0:
#         sentiment_string = "Neutral"
#     else:
#         sentiment_string = "Negative"
#     tweet_sentiments.append([tweet.text, sentiment_string])
#
# # Write the results to a CSV file
# with open("tweet_sentiments.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Tweet", "Sentiment"])
#     writer.writerows(tweet_sentiments)