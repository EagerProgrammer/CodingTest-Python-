#https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=python3
# 삼각달팽이 문제
# 첫번째 주어진 삼각형의 모양 그래프를 좌표에넣어 생각해보자(2차원 배열에)
#그리고 각 변마다 도는 규칙을 찾아보자, 찾아보면 첫번째 내려갈때 n만큼내려가고 그다음 n을 만나면 방향을 바꾸고 그다음 n-1만큰 가면 또 방향을 바꾼다는 규칙을 찾을 수 있다.
#그리고 이 방향을 바꾸는 것을 구현하기 위해 % 3을 이용 이부분 이해하는데 오래걸렸다.
def solution(n):
    result = []
    x = -1
    y = 0
    num = 1
    array = [[0]*n for _ in range(n)]
    for i in range(n):
        for _ in range(i,n): # 이부분만 이해하면 끝난다, 이부분은 range를 i,n으로 가져가면서 n-1씩 줄어들게끔 합니다.
            if i % 3 == 0: #n을 만나기전 아래로 내려가는 방향 구현
                x += 1  
                array[x][y] = num
                num += 1
            elif i % 3 == 1:#n을만나고 오른쪽으로 가는 방향 구현 후 n-1을 만나면 다시 방향 바뀌는 것을 구현
                y += 1
                array[x][y] = num
                num += 1
            elif i % 3. == 2: #n-1부터 대각선 방향으로 움직이는 것을 구현 그리고 다시 2n-1 을 만나면 다시 아래방햐으로 가는 것을 구현
                x -= 1
                y -= 1
                array[x][y] = num
                num += 1
    for i in array: #2차원 배열에서 0을 제외하고 1차원 리스트로 바꿔주는 이중 포문
        for j in i:
            if j != 0:
                result.append(j)
    return result