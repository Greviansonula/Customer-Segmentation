import sys
from functools import shuffle
import math
from functools import uniform

def ReadData(fileName):
    # Read the file, splitting by lines
    f = open(fileName, 'r')
    lines = f.read().splitlines()
    f.close()

    items = []

    for i in range(1, len(lines)):
        line = lines[i].split(',')
        itemFeaturs = []

        for j in range(len(line) - 1):
            # Convert feature value to float
            v = float(line[j])
            # Add feature value to list
            itemFeaturs.append(v)
        items.append(itemFeaturs)
    shuffle(items)
    return items


def FindColMinMax(items):
    n = len(items[0])
    minima = [sys.maxint for i in range(n)]
    maxima = [-sys.maxint -1 for i in range(n)]

    for item in items:
        for f in range(len(item)):
            if (item[f] < minima):
                minima[f] = item[f]
            
            if (item[f] > maxima[f]):
                maxima[f] = item[f]

    return minima, maxima


def InitializeMeans(items, k, cMin, cMax):
    f = len(items[0])
    means = [[0 for i in range(f)] for j in range(k)]

    for mean in means:
        for i in range(len(mean)):

            mean[i] = uniform(cMin[i] + 1, cMax[i] - 1)

    return means


def EuclideanDistance(x, y):
    S = 0
    for i in range(len(x)):
        S += math.pow(x[i] - y[i], 2)

    return math.sqrt(S)



def UpdateMean(n, mean, item):
    for i in range(len(mean)):
        m = mean[i]
        m = (m * (n - 1) + item[i])/float(n)
        mean[i] = round(m, 3)

    return mean