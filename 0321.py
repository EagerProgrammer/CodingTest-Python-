from collections import deque
def solution(arr1,arr2,N,M):
    arr3 = [[0] for _ in range(N)]
    count = 0
    for i in arr2:
        x,y = i
        arr3[y-1][x-1] = 1
    deq =deque((0,arr1))
    answer = []
    while M:
        dist,x,y = deq
        idx = [-2,-2,-1,-1,+1,+1,+2,+2]
        idy = [-1,+1,-2,2,-2,-2,-1,+1]
        for i in range(8):
            nx = idx[i] + x -1
            ny = idy[i] + y -1
            if nx >= 0 and nx <= N and ny >=0 and ny <=N:
                deq.append((dist+1,ny,nx))
                if arr3[ny][nx] == 1:
                    M -= 1
                arr3[nx][nx] = dist + 1
    for i in arr2:
        x,y = i
        result = arr3[y][x]
        answer.append(result)
    return answer


                    