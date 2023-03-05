# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 간단한 문제 수리문제였다. 둘레와 그 안의 갯수를 만들 수 있는 식을 구상해보면 쉽게 풀린다.
def solution(brown, yellow):
    brown = (brown + 4) // 2
    check = True
    x = 3 # 이부분을 생각하면 바로 풀린다.
    result = []
    for _ in range(brown):
        print(x)
        y = brown - x
        print(y)
        if (x-2) * (y-2) == yellow:
            result.append(x)
            result.append(y)
            break
        else:
            x += 1
    result.sort(reverse = True)
    return result