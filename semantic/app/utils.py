import requests
import json
from semantic.settings import API_KEY, CONSUMER_KEY, CONSUMER_SECRET
SEARCH_BASE_URL = 'https://www.googleapis.com/freebase/v1/search?key=%s' % API_KEY

def freebase_search(keyword):
	url = SEARCH_BASE_URL + '&%s' % keyword
	response = requests.get(url)
	return response.json()
