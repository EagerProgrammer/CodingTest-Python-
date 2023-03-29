# N장의 카드가 있다.
# 각각의 카드는 차례로 1 에서 N까지의 번호가 붙어 있으며 1번 카드가 가장 위 N번 카드가 가장 아래인 상태로 놓여 있다.
# 이제 다음과 같은 동작을 카드가 1 장 남을 때까지 반복한다.
import math
def solution(N):
    a = math.floor(math.log2(N))
    return 2**a

