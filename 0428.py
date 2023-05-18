def solution(arr,H):
    K = len(arr)
    N = len(arr) / H
    M = len(arr[0])
    dx = [-1,+1,0,0,0,0]
    dy = [0,0,-1,+1,0,0]
    dz = [0,0,0,0,-H,+H]
    while:
        for i in range(K):
            for k in range(M):
                if arr[i][k] == 0:
                    continue
                elif arr[i][k] == -1:
                    continue
                else:
                    for j in range(6):
                        if k + dx[j] >= 0 and k + dx[j] <= M:
                            answer = arr[i][k+dx[j]] + 1
                            if answer == 0:
                                continue
                            else:
                                arr[i][k+dx[j]] = 1
                        if i + dy[j] >=0  and i + dy[j] <= H:
                            





