#!/usr/bin/python
import requests

#http://api.wordnik.com/v4/word.json/word/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5

class Wordnik:

	def __init__(self, api_key):
		self.endpoint= 'api.wordnik.com/v4'
		self.api_key = api_key

	def getWordDefinitions(self, word, limit, related, canon, tags):
		r = requests.get('http://'+self.endpoint+'/word.json/'+word+'/definitions?limit='+limit+'&includeRelated='+related+'&useCanonical='+canon+'&includeTags='+tags+'&api_key='+self.api_key)
		return r.json()

'''wordnik = Wordnik('a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5')
json = wordnik.getWordDefinitions('word', '200', 'true', 'true', 'true')'''
