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
