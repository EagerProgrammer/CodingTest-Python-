# 2022 KAKAO Blind 채용 주자요금 계산 문제
# 주어진 자동차 입 출 시간의 배열을 split을 통해 list화 시킨 후 시간은 분단위로 바꿔 줍니다
# 그 후 배열을 자동차 번호 순과 시간 순으로 정렬합니다.
# 배열을 deque에 넣은 후 while 문으로 deque가 비울 때까지 계산합니다.
# 이 과정에서 IN OUT 이 있는 경후 Time을 dict에 추가 해주면서 더해줍니다.
# 만약 Out이 없는 경우는 11:59에 나갔다고 가정하고 계산하여 추가해줍니다.
# 마지막으로 dict의 배열 값을 순회하면서 기본요금과 단위 시간당 요금 계산을 진행하여 return 시켜 줍니다.
from collections import deque
import math
def solution(fees, records):
    dic = {}
    result = []
    answer = []
    for i in records:
        s = i.split(" ")
        result.append(s)
    for j in result:
        a = j[0].split(":")
        Time = int(a[0])*60 + int(a[1])
        j[0] = Time
    result.sort(key=lambda x:(x[1],x[0]))
    que = deque(result)
    while que:
        x,y,z = que.popleft()
        if not que and z == "IN":
            if y in dic:
                dic[y] += 1439 - x
            else:
                dic[y] = 1439 - x
            break
        for u in que:
            if y == u[1] and z == "IN" and u[2] == "OUT":
                if y in dic:
                    dic[y] += u[0] - x
                else:
                    dic[y] = u[0] - x
                que.popleft()
                break
            else:
                if y in dic:
                    dic[y] += 1439 - x
                else:
                    dic[y] = 1439 - x
                break
    preanswer = dic.values()
    for k in preanswer:
        if k < fees[0]:
            cost = fees[1]
            answer.append(cost)
        else:
            cost = math.ceil((k - fees[0]) / fees[2]) * fees[3] + fees[1]
            answer.append(cost)
    return answer
