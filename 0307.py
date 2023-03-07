# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque
import math
def solution(progresses, speeds):
    deq = deque(speeds)
    list1 = []
    result = []
    idy = 0
    for i in progresses:
        a = 100 - i 
        b = deq.popleft()
        c = math.ceil(a/b)
        list1.append(c)
    for idx in range(len(list1)): #리스트나 큐에서 한 어떤 값과 나머지 값을 비교하는것의 구현에서 애먹는다.(인덱스 및 팝 활용해야하는데 잘 활용하자....)
        if list1[idx] > list1[idy]:
            result.append(idx - idy)
            idy = idx
    result.append(len(list1) - idy)  
    return result