#처음에 푼 풀이 (시간초과)
def solution(n, left, right):
    answer = []
    array = [[0]*n for _ in range(n)]
    x = 0
    y = 0
    for _ in range(n):
        y = 0
        for j in range(n):
            if j > x:
                array[x][y] = j+1
                y += 1
            elif j <= x:
                array[x][y] = x+1
                y += 1
        x += 1
    for k in array:
        for a in k:
            answer.append(a)
    answer = answer[left:right+1]
    return answer
# 제대로 된 풀이 여기서 제한이 10에 7제곱이므로 여기서 배열을 만들어서 꺼내서 푼다는건 불가능한다는 것을 눈치 챘어야한다.!!!!!!
# 그러므로 규칙을 찾아서 풀었어야한다. 규칙은 아래와 같다.
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지 
        if a<b: a,b =b,a #큰거 구하기 
        answer.append(a+1)
    
    return answer