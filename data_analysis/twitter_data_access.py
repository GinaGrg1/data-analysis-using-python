import json
from tweepy.streaming import StreamListener, Stream, API
from tweepy import OAuthHandler

consumer_key=''
consumer_secret='L1s4zkQOpvpu0kG92eDP6DwLwqjkXT1co84DYG5udVjfqBZGYr'
access_token='891423290035666950-sXW3wgmS0Zy9x50j68viAq7ci4IeecJ'
access_token_secret='Xz9iYAdF5Wdecpzx6Nt6HqdibcvCQOLs4998xRYH6gKlF'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class PrintListener(StreamListener):
	def on_status(self, status):
		print(status.text)
		print(status.author.screen_name,
			  status.created_at,
			  status.source, 
			  '\n')

	def on_error(self, status_code):
		print("Error code: {}".format(status_code))
		return True  # Keep stream alive

	def on_time(self):
		print('Listener timed out!')
		return True  # Keep stream alive


def print_to_terminal():
	listener = PrintListener()
	stream = Stream(auth, listener)
	languages = ('en',)  # Only 
	stream.sample(languages=languages)


def pull_down_tweets(screen_name):
	api = API(auth)
	tweets = api.user_timeline(screen_name=screen_name, count=200)
	for tweet in tweets:
		print(json.dumps(tweet._json, indent=4))

if __name__ == '__main__':
	#print_to_terminal()
	pull_down_tweets(auth.username)



