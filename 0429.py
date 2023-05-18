def Solution(arr):
    a = 1
    N = len(arr)
    M = len(arr[0])
    dx = [-1,+1,0,0]
    dy = [0,0,-1,+1]
    ax = [-2,+2,0,0]
    ay = [0,0,-2,+2]
    x,y = [0,0]
    answer = []
    for _ in range(N*M):
        z = 0
        while x != M and y != N:
            for i in arr:
                if i[x][y] == 0:
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        cx = x + ax[j]
                        cy = y + ay[j]
                        if nx >=0 and nx <= M  and ny >= 0 and ny <= N:
                            if i[nx][y] == 0:
                                x = nx
                                z += 1
                                break
                            if i[x][ny] == 0:
                                y = ny
                                z += 1
                                break
                            else:
                                if a != 0:
                                    if cx >=0 and cx <= M  and cy >= 0 and cy <= N:
                                        if i[cx][y] == 0:
                                            if cx < x:
                                                x = cx + 1
                                                z += 1
                                                break
                                            else:
                                                x = cx -1
                                                z += 1
                                                break
                                        if i[x][cy] == 0:
                                            if cy < y:
                                                y = cy +1
                                                z += 1
                                                break
                                            else:
                                                y = cy -1
                                                z += 1
                                                break 
                                else:
                                    return -1
        answer.append(z)
    return min(answer)
                
