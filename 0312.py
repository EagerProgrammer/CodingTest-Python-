def solution(points,k):
    points.sort(key= lambda x: x[0]**2 + x[1]**2)
    points.sort(reverse= True)
    return points[:k]