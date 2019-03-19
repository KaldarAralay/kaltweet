import tweepy
import Tkinter
from time import sleep

consumer_key = 'YKq3ib0A753MMyDJSXWaBbCTp'
consumer_secret = 'SAKcGGIsHUBKqedQY2eKiortvBVBhpTdHmQgXN5I1nzfsdZW6r'
access_token = '1107790390160211969-ijOjYaU7qd6oGAcopUcW4lSA1EY0Qc'
access_token_secret = 'g1Mp8Vg4hPEqDom3UuwlbegRKp5OVJZkJohT53vhz65Xu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

for tweet in tweepy.Cursor(api.search, q='#runescape').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        tweet.user.follow()
	print('Followed the user')

        sleep(120)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

