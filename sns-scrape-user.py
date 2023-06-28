# SNS Scrape
!pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm.notebook import tqdm
## Pulling an exmaple tweet
scraper = sntwitter.TwitterSearchScraper('#python')

tweets = []
n_tweets = 100
for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweets):
    data = [
        tweet.user.username, 
        tweet.id, 
        tweet.date, 
        tweet.rawContent, 
        tweet.likeCount, 
        tweet.retweetCount
    ]
    tweets.append(data)
    if i > n_tweets:
        break
## Progress Bar + Export
tweet_df = pd.DataFrame(
    tweets, columns=["username", "id", "date", "rawContent", "like_count", "retweet_count"]
)

tweet_df.to_csv('python_tweets.csv', index=False, encoding='utf-8-sig')

