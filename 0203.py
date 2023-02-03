# 프로그래머스 옹알이(2) Level 2
def solution(babbling):
    answer = 0
    a = ["aya","ye","woo","ma"]
    for i in babbling:
        for j in a:
            if j*2 not in i:
                i = i.replace(j," ")
            i = i.strip()
        if len(i) == 0:
            answer +=1
    return answer