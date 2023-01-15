from helperFunctions import *

def FindClusters(mean, items):
    clusters = [[] for i in range(len(means))]

    for item in items:

        index = Classify(means, item)

        clusters[index].append(item)

    return clusters