import requests
from utils import freebase_search
from app.models import Keyword, Tweets

tweet = 'Deepika Padukone portrays the titular protagonist, a Bengali architect living in New Delhi, and Amitabh Bachchan plays her hypochondriac father'


class NGrams(object):
	"""docstring for NGrams"""
	def __init__(self, tweet):
		super(NGrams, self).__init__()
		self.tweet = tweet

	def get_bigrams(self):
		tweet = self.tweet.split()
		bigrams = [word+' '+tweet[i+1] for i, word in enumerate(tweet) if i<len(tweet)-1]
		return bigrams

	def get_trigrams(self):
		tweet = self.tweet.split()
		trigrams = [word+' '+tweet[i+1]+' '+tweet[i+2] for i, word in enumerate(tweet) if i<len(tweet)-2]
		return trigrams

def process_keywords(keywords):
	for keyword in keywords:
		res = freebase_search(keyword)
		if res['status']=='200 OK':
			if len(res['result'])>0:
				first = res['result'][0]
				if 'notable' in first:
					notable = first['notable']['name']
				else:
					notable = ''
				#score = first['score']
				keys = Keyword.objects.filter(keyword=keyword)
				if len(keys)==0:
					Keyword.objects.create(keyword=keyword, count=1, notable=notable)
				else:
					keyword_obj = keys[0]
					keyword_obj.count += 1
					keyword_obj.save()


def process_tweet(tweet):
	Tweets.objects.create(tweet=tweet)
	tweet_obj = NGrams(tweet)
	bigrams = tweet_obj.get_bigrams()
	trigrams = tweet_obj.get_trigrams()
	keywords = bigrams+trigrams
	process_keywords(keywords)