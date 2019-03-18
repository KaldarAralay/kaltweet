import tweepy
import Tkinter
from time import sleep

consumer_key = 'dCcJvgURu2OilAf77Ck6RTVZM'
consumer_secret = '5So4foAdm9WLbhzWsaFnPblVW1kATRUqXYqSBLgqMVoJJ41awR'
access_token = '1107696893688205312-83U1IMhWgBLXmBX9A4mAOafLItHVP2'
access_token_secret = 'NYQIz4EkzPdDGOfFisptSBnLLQClc5wHgGn7jpaUS78uI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

for tweet in tweepy.Cursor(api.search, q='#cybersecurity').items():
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

        sleep(500)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
