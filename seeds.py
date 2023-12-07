import random
import numpy as np
import math

#initialize centroids
def initialize_centroids(k):
    random.seed()
    k_random_centroid = []
    for x in range(k):
        k_random_centroid.append(random.randint(0 , 209))
    return k_random_centroid

#calculate euclid distance
def euclidean_distance(u , v):
    dist = 0
    for attribute in range(len(u)):
        dist += (u[attribute] - v[attribute]) ** 2
    return math.sqrt(dist)


#Read in data
with open('seeds.txt' , 'r') as file:
    data_lines = file.readlines()

seeds_data = [line.split() for line in data_lines]

seeds_data = [[float(number) for number in line] for line in seeds_data]

# 3 means clustering
centroids = initialize_centroids(3) #Our 3 data samples indices
cluster1 = []
cluster2 = []
cluster3 = []
cluster1.append(seeds_data[centroids[0]])
cluster2.append(seeds_data[centroids[1]])
cluster3.append(seeds_data[centroids[2]])


file.close()
