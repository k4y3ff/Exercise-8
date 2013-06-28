import twitter

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token_key = 'access_token_key'
access_token_secret = 'access_token_secret'

user = 'user'
api = twitter.Api(consumer_key=consumer_key, consumer_secret = consumer_secret,
    access_token_secret=access_token_secret, access_token_key=access_token_key)

statuses = api.GetUserTimeline(screen_name=user)

list_tweets = [s.text for s in statuses]
for tweet in list_tweets:
    tweet.replace('u','')
