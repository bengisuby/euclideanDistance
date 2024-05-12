def euclidean_distance(point1, point2):
    distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    return distance
   
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  


def calculate_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            distances.append(distance)
    return distances


distances = calculate_distances(points)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)
