#https://school.programmers.co.kr/learn/courses/30/lessons/148653
#이 문제애 대한 알고리즘은 생각해냈으나 실질적으로 구현하는데 실패했었다. 5일때 어떻게 처리해야하나가 고민이였다.
def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer