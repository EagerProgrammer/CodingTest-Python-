from collections import deque
def solution(arr, N):
    que = deque()
    que.append((0,0))
    visit = [[False] * N for _ in range(N)]
    cond = False
    count = []
    dx = [-1,+1,0,0]
    dy = [0,0,-1,+1]
    result = 0
    while que:
        x,y = que
        visit[x][y] = True
        for j in range(4):
            x = dx[j] + x
            y = dy[j] + y
            visited = visit[x][y]
            if x > N or x < 0 or y > N or y < 0:
                continue
            else:
                if arr[x][y] != 0 and visited != True:
                    result += 1
                    que.append((x,y))
                elif arr[x][y] == 0 and visited != True:
                    if result == 0:
                        result = 0
                    else:
                        count.append(result)
                    continue
                else:
                    break
    return count.sort()
        
    
