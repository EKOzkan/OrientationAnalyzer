import csv
import re
from textblob import TextBlob
import os

# Step 1: Read hashtags.csv
hashtags = {}
with open('hashtags.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    type_columns = header[1:]  # Extract the type columns dynamically
    types = set(type_columns)
    for row in reader:
        hashtag = row[0]
        weights = [float(value) if value else 1.0 for value in row[1:]]  # Handle weights
        weight_map = {column: weight for column, weight in zip(type_columns, weights)}
        hashtags[hashtag] = weight_map

# Step 2: Read tweets from tweets.txt and filter by hashtags
tweets_with_hashtags = []
with open('tweets.txt', 'r', encoding='utf-8') as file:
    for line in file:
        tweet = line.strip()
        for hashtag in hashtags:
            if hashtag.lower() in tweet.lower():
                tweets_with_hashtags.append(tweet)
                break

# Step 3: Sentiment analysis on tweets
sentiments = []
for tweet in tweets_with_hashtags:
    analysis = TextBlob(tweet)
    sentiment = analysis.sentiment.polarity
    sentiments.append(sentiment)

# Step 4: Calculate points based on weights
points = {type_: sum(sentiment * hashtags[hashtag].get(type_, 1.0)
                     for tweet, sentiment in zip(tweets_with_hashtags, sentiments)
                     for hashtag in hashtags
                     if hashtag.lower() in tweet.lower())
          for type_ in types}

# Step 5: Prepare data for CSV file
output_data = [['Tweet', 'Points']]
for tweet, sentiment in zip(tweets_with_hashtags, sentiments):
    output_data.append([tweet, sentiment])

# Create the 'calc' folder if it doesn't exist
folder_name = 'calc'
os.makedirs(folder_name, exist_ok=True)

# Generate the file path for the CSV
file_path = os.path.join(folder_name, 'calc.csv')

# Step 6: Save outputs to CSV file
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

# Step 7: Print results
for type_, value in points.items():
    print(f"Points ({type_}): {value:.2f}")

print(f"The tweets and their NLP points have been saved to '{file_path}' in the '{folder_name}' folder.")
