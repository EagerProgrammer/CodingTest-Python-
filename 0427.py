from heapq import heapify, heappop, heappush
def solution(arr):
    heap = []
    answer = []
    for i in arr:
        if i == 0 and len(heap) == 0:
            answer.append(-1)
        if i == 0:
            gift = heappop(heap)[1]
            answer.append(gift)
        else:
            i.pop(0)
            for k in i:
                heappush(heap, (-k,k))
    return answer


