#https://school.programmers.co.kr/learn/courses/30/lessons/12987
#A와 B를 비교했을 때 각각 원소를 비교하는데 B가 더 크면 승정 1을 가지고 승점의 최대값을 가질때 return한다.
#중요 알고리즘 : 오름차순으로 정렬 후 B를 A와 비교할때 작으면 A의 최대값과 비교해서 소모해버리는 알고리즘 Deque를 활용하여 해결
from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    while B:
        if A[0] < B[0]:
            answer += 1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
    return answer