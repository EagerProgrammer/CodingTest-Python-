##https://school.programmers.co.kr/learn/courses/30/lessons/176963
##문제는 dic와 for문을 돌면서 없는 단어에 대한 예외 처리만 해주면 쉽게 끝나는 문제입니다.
def solution(name, yearning, photo):
    dic = {}
    x = 0
    answer = []
    for i in range(len(name)):
        if i > len(yearning)-1:
            dic[name[i]] = 0
        dic[name[i]] = yearning[i]
    for j in photo:
        for a in j:
            if a not in name:
                continue
            y = dic[a]
            x += y
        answer.append(x)
        x = 0
    return answer