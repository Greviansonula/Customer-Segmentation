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


def Classify(means, item):
    # Classify item to the mean with minimum distance
    minimum = sys.maxint
    index = -1

    for i in range(len(means)):
        dis = EuclideanDistance(item, means[i])

        if (dis < minimum):
            minimum = dis
            index = i

    return index


def calculateMeans(k, items, maxIterations=10000):
    # Find the minima and maxima for colums
    cMin, cMax = FindColMinMax(items)

    # Initialize means at random points
    means = InitializeMeans(items, k, cMin, cMax)

    # initialize clusters, the array to hold the number of items
    # in a class
    clusterSizes = [0 for i in range(len(means))]

    # An array to hold the cluster an item belongs
    belongsTo = [0 for i in range(len(items))]

    # Calculate means
    for e in range(maxIterations):

        # if no change of clusetr occurs, halt
        noChange = True
        for i in range(len(items)):
            item = items[i]

            index = Classify(means, item)

            clusterSizes[index] += 1
            cSize = clusterSizes[index]
            means[index] = UpdateMean(cSize, mean[index], item)

            if (index != belongsTo[i]):
                noChange = False

            belongsTo[i] = index
        
        # Nothing changd, return
        if (noChange):
            break
    
    return means

