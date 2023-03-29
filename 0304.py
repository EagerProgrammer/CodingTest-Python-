#주식 팔고 사기 좋은 시기
#제한 조건 시간복잡도 N^2 안 넘기
from collections import deque
def solution(array):
    answer = 0
    deq = deque(array)
    x = 1000001
    while deq:
        y = deq.popleft()
        a = min(x,y)
        answer = max(answer, y - a)
        x = y
    return answer

        