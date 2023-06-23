##https://school.programmers.co.kr/learn/courses/30/lessons/135808
##내림차순으로 정렬 후 m만큼 끊어서 생각한다. 이 때 max값이 k보다 크면 계산하지 않고 나머지는 최소값에 m개수 만큼 합을 추가해준다.
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    x = len(score)
    for j in range(1,(x//m)+1):
        temp = score[m*j-m:m*j]
        if max(temp) > k:
            continue
        else:
            answer += min(temp)*m
    return answer