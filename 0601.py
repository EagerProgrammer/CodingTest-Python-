#https://school.programmers.co.kr/learn/courses/30/lessons/155651
#맨 처음에 dict을 통해서 풀려고 했는데 그렇게 되면 재귀를 써야했고, for 문이 너무 많아져서 문제라고 생각했다.
#그래서 힌트를 보고 heapq로 접근했다. 우선 주어진 호텔 대실 리스트르 시간 정수로 바꾼다음, heapq에 넣어주면서 heapq에 퇴실시간 + 10을 넣어줄껀데, 그게 다음 입실 시간보다 작으면 pop으로 제거 아니면 answer +=1 을 하며 객실을 추가해준다.
from heapq import heappop, heappush
def solution(book_time):
    answer = 0
    for i in book_time:
        for j in range(len(i)):
            temp = i[j].split(":")
            result = int(temp[0])*60+int(temp[1])
            i[j] = result
    book_time.sort(key=lambda x:(x[0],x[1]))
    heap = []
    for s, e in book_time:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    return answer+1