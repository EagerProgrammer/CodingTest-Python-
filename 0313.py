from collections import deque
def solution(arr,M,N):
    idx = [-1,1,0,0]
    idy = [0,0,1,-1]
    deq = deque([0,0,1])
    answer = 0
    while deq:
        x,y,start = deq
        for i in range(4):
            x = idx[i] + x
            y = idy[i] + y
            if x < M and x > 0 and y < N and y > 0:
                if arr[x][y] == 0:
                    break
                else:
                    start += 1
                    deq = deque([x,y,start])
            else:
                continue
        answer = start
    return answer
