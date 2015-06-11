#!/usr/bin/python
import math

class ListMath:

	def __init__(self, numbers):
		self.numbers = numbers

	def getRange(self):
		return max(self.numbers) - min(self.numbers)

	def getMean(self):
		return sum(self.numbers) / len(self.numbers)

	def getVariance(self, mu=None, type="sample"):
		variance = 0
		if mu is None:
			mu = self.getMean()
		if type == "sample":
			mod = 1
		else:
			mod = 0
		return sum((xi-mu)**2 for xi in self.numbers) / (len(self.numbers) - mod);

	def getStandardDeviation(self):
		return math.sqrt(self.getVariance())
		
		
		



'''mylist = ListMath([1, 2, 3, 4, 5, 6, 7, 8, 9]) #instanciate math list
print('RANGE: ', mylist.getRange()) #get list range
print('MEAN: ', mylist.getMean()) #get list mean
print('VARIANCE: ', mylist.getVariance()) #get list variance
print('STANDARD DEV: ', mylist.getStandardDeviation()) #get list standard deviation'''
