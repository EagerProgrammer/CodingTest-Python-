#https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque #캐시의 리스트에서 큐 및 스택 처럼 동작해야하므로 바로 deque를 사용
def solution(cacheSize, cities):
    count = 0 #결과를 도출하기 위해 셋팅
    deq = deque() # Cache 역할을 할 deque
    for i in cities:
        i = i.upper() # 대소문자 신경쓰기 싫어서 순회하면서 다 대문자로 치환
        if cacheSize == 0: # 캐시사이즈가 0이면 더 이상 고려할 필요가 없어서
            count = len(cities) * 5
        elif len(deq) < cacheSize: # Cacher가 다 안찼을 경우
            if deq.count(i) != 1:
                deq.append(i)
                count += 5
            else:
                deq.remove(i) # 캐시의 deque안에서도 LRU를 구현해야하므로 최근 사용한것을 젤 앞으로
                deq.append(i)
                count += 1
        elif len(deq) >= cacheSize: # 캐시가 이제 꽉찼을 때
            if deq.count(i) != 1:
                deq.popleft()
                deq.append(i)
                count += 5
            else:
                deq.remove(i)
                deq.append(i)
                count += 1
    return count