from collections import deque
from heapq import heappop, heappush
def solution(N,arr):
    rep = True
    heap = []
    answer = 0
    compare1 = 0 
    compare2 = 0 
    candidate = deque(arr)
    criminal = candidate.popleft()
    candidate2 = list(candidate)
    for num in candidate2:
        heappush(heap, (-num, num))
    while rep == False:
        if compare1 == 0:
            compare1 = heappop(heap)
        else:
            compare1 = compare2
        compare2 = heappop(heap)
        temp = compare1 - compare2
        if (criminal + temp) > compare2:
            rep = True
            answer += temp
        else:
            answer += temp
    return answer

