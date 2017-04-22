import json

import os
import twitter
from elasticsearch import Elasticsearch

#
# Create Twitter Stream by Twitter OAuth in OS environment.
#
def connect_twitter_stream():
    """
    You need to set os environment like 'export TWITTER_CONSUMER_KEY=YOUR KEY'.
    """
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    auth = twitter.OAuth(token=access_token,
                         token_secret=access_secret,
                         consumer_key=consumer_key,
                         consumer_secret=consumer_secret)
    return twitter.TwitterStream(auth=auth)


def put_stream(es, twitter_stream):
    tweets = twitter_stream.statuses.sample()
    # tweets = twitter_stream.statuses.filter(track='Google', language="ja")
    for tweet in tweets:
        try:
            if 'lang' in tweet and tweet['lang'] == 'ja':
                dic = {
                    'tweet_id': tweet['id'],
                    'screen_name': tweet['user']['screen_name'],
                    'text': tweet['text']
                }
                if tweet['entities']['hashtags']:
                    # hash tags is array.
                    dic['hashtags'] = tweet['entities']['hashtags']

                es.index(index="twitter", doc_type='tweet', body=dic)
                # dict to JSON.
                print(json.dumps(dic, ensure_ascii=False))
        except:
            import traceback
            traceback.print_exc()
            pass


if __name__ == '__main__':
    es = Elasticsearch()
    twitter_stream = connect_twitter_stream()
    put_stream(es, twitter_stream)
