#!/usr/bin/python
import csv
import math
import operator

#Distance Formulae
'''
Pythagorean Theorum: c^2 = a^2 + b^2
Euclidean Distance (one dimension): d = sqrt((y1-y2)**2 + (x1-x2)**2)
Euclidean Distance (multi dimension): d = sqrt(sum(x=1..n, (Dx)**2))
Jacard Distance: J(A,B) = AnB/AuB #A and B are sets of words from two docs (n=words in common, u=unique words)
Manhattan Distance: M = (x1-x2) + (y1-y2)
'''

#clean csv
'''
iconv -f utf-8 -t utf-8 -c file.dirty.csv > file.clean.csv
'''

class Algo:

    def __init__(self):
        self.training_set_dirty=[]
        self.training_set=[]
        self.test_set=[]

    def loadTrainingSet(self, filename, key):
        with open(filename, 'rt') as csvfile:
            lines = csv.reader(csvfile)
            for line in lines:
                self.training_set_dirty.append(line)

            for x in range(len(self.training_set_dirty)):
                self.training_set.append([])
                for y in key:
                    try:
                        val = self.training_set_dirty[x][y.get('index')]
                        if 'conversion' in y:
                            for convert in y.get('conversion'):
                                val.replace(convert.get('from'), convert.get('to'))

                        if y.get('type') == 'float':
                            val = float(val)
                        if y.get('type') == 'string':
                            val = str(val)
                    except:
                        val = 0.00
                       
                    self.training_set[x].append(val)

    def loadTestSet(self, test_set):
        self.test_set=test_set

    def getEuclideanDistance(self, x, y):
        distance = 0
        for i in range(len(x) - 1):
            distance += (float(x[i] - y[i]))**2

        return math.sqrt(distance)
         

    def getKNearestNeighbor(self, k):
        distances=[]
        for sample in self.training_set:
            distances.append((sample, self.getEuclideanDistance(sample, self.test_set)))
        
        distances.sort(key=operator.itemgetter(1))
        neighbors=[]
        for x in range(k):
            neighbors.append(distances[x][0])

        return neighbors

'''algo = Algo()
algo.loadTrainingSet('/var/python/ga/dat-la-07/hw/hw1-athletes.clean.csv', 
    [
        {'index': 2, 'name': 'age', 'type': 'float'},
        {'index': 3, 'name': 'height', 'type': 'float'},
        {'index': 4, 'name': 'weight', 'type': 'float'},   
        #{'index': 5, 'name': 'sex', 'type': 'float', 'conversion': [{'from': 'F', 'to': 0},{'from':'M', 'to': 1}]},
        #{'index': 8, 'name': 'gold', 'type': 'float'}, 
        #{'index': 9, 'name': 'bronze', 'type': 'float'}, 
        #{'index': 10, 'name': 'silver', 'type': 'float'}, 
        {'index': 12, 'name': 'sport', 'type': 'string'}
    ]
)
algo.loadTestSet([27, 182, 104])
print(algo.getKNearestNeighbor(3))'''
