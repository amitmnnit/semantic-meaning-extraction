import requests
from utils import freebase_search

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

		