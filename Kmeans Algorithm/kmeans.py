from helperFunctions import *
import numpy as np

def FindClusters(means, items):
    clusters = [[] for i in range(len(means))]

    for item in items:

        index = Classify(means, item)

        clusters[index].append(item)

    return clusters

items = ReadData("data.txt")

means = calculateMeans(3, items)

clusters = FindClusters(means, items)

print(clusters)