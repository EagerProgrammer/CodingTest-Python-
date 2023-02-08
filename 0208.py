#https://school.programmers.co.kr/learn/courses/30/lessons/62048
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
# 이건 완전 수리능력이였디. 풀이를 보면 이처럼 간단할 수가 없다. 좌표에 옮겨서 생각해보자. 그리고 공약수가 있을 때 없을 때로 나눠서 과연 몇개의 사각형이 잘리는지를 보면 규칙을 찾을 수있다.
