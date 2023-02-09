#https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    price = deque(prices) #list를 deque으로 바꾸는 과정
    answer = []
    for _ in range(len(price)):
        a = price.popleft() #인덱스 순으로 꺼내기 위해 popleft로 꺼내며 비교할 대상이므로 a에 할당해주기
        count = 0
        if len(price) == 0: #마지막은 비교할 남은 대상들이 없으므로 0으로 처리
            count = 0
        for i in price: #비교를 위한 주체를 빼고 나머지가 있는 deque를 순회
            if a <= i:
                count +=1 # 나보다 더 크거나 같으면 떨어진게 아니므로 카운트
            else:
                count += 1  #나보다 작으면 떨어진거지만 1초 버틴걸로 치기에 카운트 1하고 브레이크로 탈출
                break
        answer.append(count) #결과를 리스트로 반환
    return answer