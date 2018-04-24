from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from data_crawler_helper import twitter_credentials
from os.path import *
import csv
import json

base_dir = dirname(dirname(abspath(__file__)))
csvFile = open(base_dir + '/tweets_features/tweets.csv', 'a')
csvWriter = csv.writer(csvFile)
#csvWriter.writerow(["created_at", "id_str", "text"])
class TwitterStreamer():

    '''
    streaming and processing love tweets.
    '''
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #This handles Twitter authentication and the connection  to the twitter streaming API
        listener = StdOutListener(fetched_tweets_filename)

        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list, languages=["en"])

class StdOutListener(StreamListener):

    '''
    Basic listener class that print the steamed tweets.
    '''

    def __init__(self, fetched_tweets_filename):
        super(StdOutListener, self).__init__()
        self.fetched_tweets_filename = fetched_tweets_filename
        self.number_of_collected_tweets = 0


    def on_data(self, raw_data):
        try:
            raw_data = json.loads(raw_data)

            csvWriter.writerow([str(raw_data["created_at"]).replace(",", ""), str(raw_data["id_str"]).replace(",", ""), str(raw_data["text"].encode('utf-8')).replace(",", "")])

            self.number_of_collected_tweets += 1
            print("%s tweets crawled..." % str(self.number_of_collected_tweets))
            if self.number_of_collected_tweets >= 900000:
                csvFile.close()
                return False

        except BaseException as e:
            print("Error on_data: %s" %str(e))

        return True


    def on_error(self, status_code):
        print(status_code)