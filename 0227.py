# https://school.programmers.co.kr/learn/courses/30/lessons/140107
# 처음에 좌표를 모두 구해서 하나씩 피타고라스로 거리를 측정해서 답을 구했지만 역시 시간 초괴
# 밑에 풀이는 답안 참조한것
def solution(k, d):
    answer = 0
    for x in range(0,d+1,k):
        res = int((d**2 - x**2)**0.5) #x좌표를 주어진 조건에 맞게 증가시킨다. 그리고 그때 최대 거리인 d안에 들어가는 y좌표들을 구한다. 이것을 반복해주면 끝
        answer += (res // k) + 1        
        
    return answer