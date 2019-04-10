# -*- coding: utf-8 -*-
import tweepy
import Tkinter
from time import sleep
import config
from config import consumer_key1, consumer_secret1, access_token1, access_token_secret1



	

consumer_key = consumer_key1
consumer_secret = consumer_secret1
access_token = access_token1
access_token_secret = access_token_secret1

topic = ''
sTime = 0

print(" ____  __.  _____  .____  _____________      ___________________________________")
print("|    |/ _| /  _  \ |    | \__    ___/  \    /  \_   _____/\_   _____/\__    ___/")
print("|      <  /  /_\  \|    |   |    |  \   \/\/   /|    __)_  |    __)_   |    |   ")
print("|    |  \/    |    \    |___|    |   \        / |        \ |        \  |    |   ")
print("|____|__ \____|__  /_______ \____|    \__/\  / /_______  //_______  /  |____|   ")
print("        \/       \/        \/              \/          \/         \/            ")


def menu():
	print("1) Retweet, Follow, Unfollow(Gain followers and build content)")
	print("2) Follow, Unfollow(Gain followers without following others)")
	print("3) Retweet, Follow(Gain followers, Follow others, Retweet content)")
	print("4) Follow all followers")
	print("5) Search user by screenname")
	print("6) Your stats and info")
	print("0) Exit")
	
	input  = raw_input("Enter Selection... ")
	
	
	if input == "1":
		try:
			topic = raw_input('Enter topic to find followers: #')
			sTime = int(raw_input("Enter time between each action(in seconds):"))

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

			user = api.me()
			

		

			for tweet in tweepy.Cursor(api.search, q='#'+topic).items():
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
					
					print 'Sleeping ',sTime,' Seconds'
					sleep(sTime)
					
					tweet.user.unfollow()
					print('Unfollowed the user')

				except tweepy.TweepError as e:
					print(e.reason)

				except StopIteration:
					break
		except Exception:
			
			print("\n")
			print("ERROR")
			print("\n")
		
				
			menu()
	if input == "2":
		try:
			topic = raw_input('Enter topic to find followers: #')
			sTime = int(raw_input("Enter time between each action(in seconds):"))

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

			user = api.me()
			


			for tweet in tweepy.Cursor(api.search, q='#'+topic).items():
				try:
					print('\nTweet by: @' + tweet.user.screen_name)


					# Follow the user who tweeted
					tweet.user.follow()
					print('Followed the user')
					
					print 'Sleeping ',sTime,' Seconds'
					sleep(sTime)
					
					tweet.user.unfollow()
					print('Unfollowed the user')

				except tweepy.TweepError as e:
					print(e.reason)

				except StopIteration:
					break
		except Exception:
			
			print("\n")
			print("ERROR")
			print("\n")
		
				
			menu()
	if input == "3":
		try:
			topic = raw_input('Enter topic to find followers: #')
			sTime = int(raw_input("Enter time between each action(in seconds):"))

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

			user = api.me()
			


			for tweet in tweepy.Cursor(api.search, q='#'+topic).items():
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
					
					print 'Sleeping ',sTime,' Seconds'
					sleep(sTime)
					

				except tweepy.TweepError as e:
					print(e.reason)

				except StopIteration:
					break
		except Exception:
			
			print("\n")
			print("ERROR")
			print("\n")
		
				
			menu()
	if input == "4":
		try:
			

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

			user = api.me()
			print(user.name)


			for follower in tweepy.Cursor(api.followers).items():
				follower.follow()
				print("Following " + follower.screen_name)
				
			
			
				
		except Exception:
			
			print("\n")
			print("ERROR")
			print("\n")
		
				
			menu()
	if input == "6":
		try:
			

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

			user = api.me()
			print 'Username: ',user.name
			print 'Screen name: ',user.screen_name
			print 'User ID number: ',user.id
			
			print 'API key: ',consumer_key
			print 'API secret key: ',consumer_secret
			print 'Access token: ',access_token
			print 'Access token secret: ',access_token_secret
			print 'Location: ',user.location
			#print 'Metadata: ',user.derived
			print 'Verified: ',user.verified
			print 'Follower Count: ',user.followers_count
			print 'Friends Count: ',user.friends_count
			print 'Public lists: ',user.listed_count
			print 'Favorited tweets: ',user.favourites_count
			print 'Statuses: ',user.statuses_count
			print 'Description: ',user.description
			print 'Protected tweets: ',user.protected
			print 'Created: ',user.created_at
			print 'Geo enabled: ',user.geo_enabled
			print 'Language: ',user.lang
			print 'Contributor mode: ',user.contributors_enabled
			print 'Background image URL(http): ',user.profile_background_image_url
			print 'Background image URL(https): ',user.profile_background_image_url_https
			#print 'Banner URL URL(http): ',user.profile_banner_url
			print 'Profile image URL(http): ',user.profile_image_url
			print 'Profile image URL(https): ',user.profile_image_url_https
			print 'Default profile image: ',user.default_profile_image
			#print 'Withheld in countried: ',user.withheld_in_countries
			
			
			print('################################################################')
			menu()		

				
		except Exception:
			
			print("\n")
			print("ERROR")
			print("\n")
		
				
			menu()
	if input == "5":
		try:
			

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
			
			nSearch = raw_input('Enter screenname to search: ')

			user = api.get_user(nSearch)
			print 'Username: ',user.name
			print 'Screen name: ',user.screen_name
			print 'User ID number: ',user.id
			print 'Location: ',user.location
			#print 'Metadata: ',user.derived
			print 'Verified: ',user.verified
			print 'Follower Count: ',user.followers_count
			print 'Friends Count: ',user.friends_count
			print 'Public lists: ',user.listed_count
			print 'Favorited tweets: ',user.favourites_count
			print 'Statuses: ',user.statuses_count
			print 'Description: ',user.description
			print 'Protected tweets: ',user.protected
			print 'Created: ',user.created_at
			print 'Geo enabled: ',user.geo_enabled
			print 'Language: ',user.lang
			print 'Contributor mode: ',user.contributors_enabled
			print 'Background image URL(http): ',user.profile_background_image_url
			print 'Background image URL(https): ',user.profile_background_image_url_https
			#print 'Banner URL URL(http): ',user.profile_banner_url
			print 'Profile image URL(http): ',user.profile_image_url
			print 'Profile image URL(https): ',user.profile_image_url_https
			print 'Default profile image: ',user.default_profile_image
			#print 'Withheld in countried: ',user.withheld_in_countries
			
			
			print('################################################################')
			
			menu()		

				
		except Exception:
			
			print("\n")
			print("ERROR, PROFILE NOT FOUND")
			print("\n")
		
				
			menu()
			
menu()