import twitter

consumer_key = 'consumer_key' # Enter consumer key here
consumer_secret = 'consumer_secret' # Enter consumer secret here
access_token_key = 'access_token_key' # Enter public access token key here
access_token_secret = 'access_token_secret' # Enter secret access token here

user = 'user'

api = twitter.Api(consumer_key=consumer_key, consumer_secret = consumer_secret,
    access_token_secret=access_token_secret, access_token_key=access_token_key)


users = ['S_C_','kanyewest','Tip','Eminem','nickiminaj','LilTunechi']
tweets=[]
for user in users:
    object_statuses = api.GetUserTimeline(screen_name=user)
    user_status = [s.text for s in object_statuses]
    tweets.extend(user_status)


for i in tweets:
    print i

