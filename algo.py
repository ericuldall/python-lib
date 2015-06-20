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

#normalize data
'''
x = x-min/max-min
'''

#clean csv
'''
iconv -f utf-8 -t utf-8 -c file.dirty.csv > file.clean.csv
'''

class Algo:

    def __init__(self):
        self.is_normal=True
        self.training_set_dirty=[]
        self.training_set=[]
        self.training_set_min=[]
        self.training_set_max=[]
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

    def useNormalData(self, is_normal):
        self.is_normal = bool(is_normal)

    def getTrainingSetRanges(self):
        self.training_set.sort(key=operator.itemgetter(0))
        self.training_set_min.append(self.training_set[0][0])
        self.training_set_max.append(self.training_set[-1][0])
        self.training_set.sort(key=operator.itemgetter(1))
        self.training_set_min.append(self.training_set[0][1])
        self.training_set_max.append(self.training_set[-1][1])
        self.training_set.sort(key=operator.itemgetter(2))
        self.training_set_min.append(self.training_set[0][2])
        self.training_set_max.append(self.training_set[-1][2])

    def loadTestSet(self, test_set):
        self.test_set=test_set

    def getEuclideanDistance(self, x, y):
        distance = 0
        for i in range(len(x) - 1):
            if self.is_normal:
                distance += float(((x[i]-self.training_set_min[i])/(self.training_set_max[i]-self.training_set_min[i])) - ((y[i]-self.training_set_min[i])/(self.training_set_max[i]-self.training_set_min[i])))**2
            else:
                distance += (float(x[i] - y[i]))**2

        return math.sqrt(distance)
         

    def getKNearestNeighbor(self, k, training_set=None, test_set=None):
        training_set = self.training_set if training_set is None else training_set
        test_set = self.test_set if test_set is None else test_set
        distances=[]
        for sample in training_set:
            distances.append((sample, self.getEuclideanDistance(sample, test_set)))
        
        distances.sort(key=operator.itemgetter(1))
        neighbors=[]
        for x in range(k):
            neighbors.append(distances[x][0])

        return neighbors

    def xrefTrainingSet(self, k):
        success = 0
        iterations = 0
        for sample in self.training_set:
            xref_test_set=sample
            xref_training_set=[]
            for xref_sample in self.training_set:
                if xref_test_set != xref_sample:
                    xref_training_set.append(xref_sample)
            
            neighbors = self.getKNearestNeighbor(k, xref_training_set, xref_test_set)
            for neighbor in neighbors:
                if neighbor[3] == xref_test_set[3]:
                    success += 1
                    break;

            iterations += 1
            
            print(xref_test_set[3], [x[3] for x in neighbors])
            print(success, ' out of ', iterations, ' were successfully matched!')


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
#algo.getTrainingSetRanges()
algo.useNormalData(False)
#print(algo.getKNearestNeighbor(3))
print(algo.xrefTrainingSet(3))'''
