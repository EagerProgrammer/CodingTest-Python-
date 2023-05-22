#https://school.programmers.co.kr/learn/courses/30/lessons/42890
#맨 처음 이문제를 보고 나는 dict을 활용해서 인덱스별로 체크하고 set을 이용해 중복을 제거해도 len(relation)이랑 같으면 result에 추가할라고 했다
#근데 무선 모든 경우의 수를 다해야 하는데 그래서 for문을 돌려야한다 생각했는데 진짜 combinatio으로 경우의 수를 다 구하고 구해야했다
#그리고 최소성을 어떻게 처리해줘야 했는데 유일성을 만족한 것들 중에서 또 for문을 돌면서 교집합들이 unique를 만족하는지 체크한다.(이부분을 생각 못했습니다.)
from itertools import combinations
def solution(relation):
    col = len(relation[0])
    # 전체 조합
    all_case = []
    for k in range(1, col + 1):
        all_case.extend(combinations(range(col), k))

    # 유일성
    unique = []
    for case in all_case:
        temp = ["".join(relate[int(idx)] for idx in case) for relate in relation]
        if len(set(temp)) == len(relation):
            unique.append(case)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            # if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
    return len(answer)