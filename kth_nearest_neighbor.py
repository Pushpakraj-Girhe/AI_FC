from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def kth_nearest_neighbor(data, query, k):
    distances = sorted(data, key=lambda point: euclidean_distance(point, query))
    return distances[k-1] if k <= len(distances) else None

# Example usage
data_points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1)]
query_point = (6, 5)
k = 2
print("K-th Nearest Neighbor:", kth_nearest_neighbor(data_points, query_point, k))

===================================================================================
dataSet:: (2, 3), (5, 4), (9, 6), (4, 7), (8, 1)
query_point = (6, 5)
use the distannce fromula here the sqrt((X2-X1)^2 + (Y2-Y1)^2)
calculate for each query to each dataSet
like below::

(2,3) → 4.47

(5,4) → 1.41

(9,6) → 3.16

(4,7) → 2.83

(8,1) → 4.47

now sort them and take the kth point as output::so the take kth result from this answer
