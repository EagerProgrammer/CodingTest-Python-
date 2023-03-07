#https://school.programmers.co.kr/learn/courses/30/lessons/42885
#문제 조건좀 제대로 읽자...보트에 최대 2명인데 2명이상 태울 수 있는줄 알고 계속 풀고 있었다...
#list로 풀어도 ㄱㅊ고 deq으로 풀어도 상관없다. 주의할 점은 두개를 pop하는 경우가 있으므로 empty deque를 조심해서 조건 설정할 것
from collections import deque

def solution(people, limit):
    count = 0
    people.sort()
    q = deque(people)
    w = 0
    cnt = 0
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                count += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                count += 1
        else:
            if q[0] <= limit:
                q.pop()
                count += 1
    return count