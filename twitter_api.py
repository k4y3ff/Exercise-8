'''
Tweets from multiple users' timelines
'''

import twitter

consumer_key = 'consumer_key' # Enter consumer key here
consumer_secret = 'consumer_secret' # Enter consumer secret here
access_token_key = 'access_token_key' # Enter public access token key here
access_token_secret = 'access_token_secret' # Enter secret access token here

users = ['users']

def stream_timelines(consumer_key,consumer_secret,access_token_secret,access_token_key):

    api = twitter.Api(consumer_key=consumer_key, consumer_secret = consumer_secret,
        access_token_secret=access_token_secret, access_token_key=access_token_key)

    tweets=[]

    for user in users:
        object_statuses = api.GetUserTimeline(screen_name=user,include_rts=False)
        user_status = [s.text for s in object_statuses]
        tweets.extend(user_status)


    tweets = " ".join(tweets)
    word_list = tweets.split()

    for bad_guy in ["http","@","RT","&","&amp"]:
        word_list[:] = [word for word in word_list if word[0:len(bad_guy)] != bad_guy]    


    clean_tweets = " ".join(word_list)

    encoded_tweets = clean_tweets.encode(encoding='UTF-8') #apparently this gets rid of the 'u's

    textfile = file('input_file.txt','w')
    textfile.write(encoded_tweets)


stream_timelines(consumer_key,consumer_secret,access_token_secret,access_token_key)