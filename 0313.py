from collections import deque
def solution(arr,M,N):
    idx = [-1,1,0,0]
    idy = [0,0,1,-1]
    deq = deque([0,0,1])
    answer = 0
    while deq:
        x,y,start = deq
        for i in range(4):
            nx = idx[i] + x
            ny = idy[i] + y
            if nx < M and nx > 0 and ny < N and ny > 0:
                if arr[nx][ny] == 0:
                    break
                else:
                    start += 1
                    deq = deque([x,y,start])
            else:
                continue
        answer = start
    return answer
 