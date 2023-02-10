#https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 파이썬에서 heapq가 있는지 몰랐다. 알아서 재정렬을 하는 list라 생각하면 된다. 그래서 내가 굳이 sort를 해주지않아도 ㄱㅊ아서 훨씬 시간 복잡도가 좋음
# 아래는 답안이다.. deque로 풀려다가 시간초과 떴다...다시 풀어보자 heapq의 활용이 중요
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer