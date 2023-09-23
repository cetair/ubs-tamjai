# from scipy.spatial import KDTree

# require to go through all q 
# starts from (0,0)

# {
#    "k": 10,
#    "p": [[0, 0], [0, 100], [100, 0], [100, 100]],
#    "q": [[1, 0], [1, 100], [ 99, 0], [ 99, 100]]
# }
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

p = [[0, 0], [0, 100], [100, 0], [100, 100]]
q = [[1, 0], [1, 100], [ 99, 0], [ 99, 100]]


def teleportation(p,q):
    dist = []
    for i in range(len(q)):
        temp = 9999
        print("q",i, ":", q[i]) 
        for j in range(len(p)):
            distance = euclidean_distance(p[j], q[i])
            if (distance < temp): 
                temp = distance 
        dist.append(temp)
    
    sum = 0
    for k in range(len(dist)):
        sum += dist[k]
    print("sum", sum)
    return sum


if __name__ == "__main__":
    teleportation([[0, 0], [0, 100], [100, 0], [100, 100]],[[1, 0], [1, 100], [ 99, 0], [ 99, 100]])
