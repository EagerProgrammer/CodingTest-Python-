#https://school.programmers.co.kr/learn/courses/30/lessons/42884
#코드는 단순하다, Greedy 문제였기 때문에 알고리즘만 잘 생각했다면 문제는 풀 수 있다.
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer