from twitter_scraper import get_tweets
import datetime
import csv

# Set the hashtag and date range
hashtag = '#BlackLivesMatter'
start_date = datetime.date(2020, 5, 30)
end_date = datetime.date(2020, 6, 2)

# Create a list to store the tweets
tweets = []

# Iterate through the tweets using the get_tweets() function
for tweet in get_tweets(hashtag, pages=20):
    tweet_date = tweet['time'].date()
    # Check if the tweet date is within the desired range
    if start_date <= tweet_date <= end_date:
        tweets.append(tweet)

# Write the tweets to a CSV file
with open('black_lives_matter_tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'mood', 'score'])
    mood = ""
    score = 0
    for tweet in tweets:
        writer.writerow(tweet['time'], mood, score)
