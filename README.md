# Twitter Crawler

This is a twitter crawler that can crawl football (soccer) related data so we can use them to train any machine learning model to be able to detect intent and entity recognition.
It's based on Tweepy, a twitter streaming framework.
## Keywords used:

We are crawling tweets which include key words about football related to these countries:

Note that, the dictionaries are not so accurate, but this will not make big difference because we will mix them afterall.


# How it works

It starts a streamer which listens to twitter api and crawl any tweets published including any keywords frmo the proposed ones.
 
## Running
Run this to start crawling, and the crawled stream will be saved in ```tweets_features/tweets.csv```
```bash
$python3 crawler_entrypoint/crawler.py
```

## Re-use it

You can add/remove keywords, just add new field in the ```dictionary``` provided in ```crawler_entrypoint/crawl.py```

## Further improvements

For further improvements, these tutorials can help improving the crawler:

- Twitter API with Python: Part 1 -- Streaming Live Tweets: https://www.youtube.com/watch?v=wlnx-7cm4Gg
- Twitter API with Python: Part 2 -- Cursor and Pagination: https://www.youtube.com/watch?v=rhBZqEWsZU4

## Configurations used
- Twitter app used: https://apps.twitter.com/app/15130100/keys