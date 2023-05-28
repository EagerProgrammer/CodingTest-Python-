#https://school.programmers.co.kr/learn/courses/30/lessons/172927
#문제는 dic과 반복문을 활용한 구현 문제이다.
#나는 먼저 곡괭이의 수를 확인한 후 최대 캘 수 있는 광물 수를 정의한 후
#dicr과 배열을 5로 나눠서 광물의 숫자를 dic에 담았다
#그후 dia, iron, stone 순으로 피로도 높은 순으로 정렬시켰다
#그 후 하나씩 꺼낸다음에 picks의 곡괭이에 맞게 피로도를 카운트 한다.
import math
from collections import deque
def solution(picks, minerals):
    can = 5 * sum(picks)
    dic = {}
    answer = 0
    if can < len(minerals):
        for i in range(math.ceil(can/5)):
            temp = minerals[i*5:(i+1)*5]
            dia = temp.count("diamond")
            ir = temp.count("iron")
            st = temp.count("stone")
            dic[i] = [dia,ir,st]
    else:
        for i in range(math.ceil(len(minerals)/5)):
            temp = minerals[i*5:(i+1)*5]
            dia = temp.count("diamond")
            ir = temp.count("iron")
            st = temp.count("stone")
            dic[i] = [dia,ir,st]
    result = list(dic.values())
    result.sort(key= lambda x:(x[0],x[1],x[2]), reverse = True)
    que2 = deque(result)
    while que2:
        c = que2.popleft()
        for i in range(len(picks)):
            if i == 0 and picks[i] != 0:
                picks[i] -= 1
                answer += sum(c)
                break
            elif i == 1 and picks[i] != 0:
                picks[i] -= 1
                answer += c[0]*5
                answer += c[1]+c[2]
                break
            elif i == 2 and picks[i] != 0:
                picks[i] -= 1
                answer += c[0]*25
                answer += c[1]*5
                answer += c[2]
                break         
    return answer