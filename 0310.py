#https://school.programmers.co.kr/learn/courses/30/lessons/67258
#정확도는 100프로인데 효율성에서 0점이다....다른 알고리즘으로 풀어야겠다. 왜일까..ㅠㅠㅠㅠㅠㅠㅠㅠ물어봐야겠다
def solution(gems):
    set1 = set(gems)
    a = len(set1)
    answer = []
    for i in range(len(gems)):
        count = 1
        dic1 = {}
        dic1[gems[i]] = i
        for j in range(i+1,len(gems)):
            if count != a:
                if dic1.get(gems[j]) == None:
                    dic1[gems[j]] = j
                    count += 1
                    if count == a:
                        answer.append([i+1,j+1])
                else:
                    continue
            else:
                answer.append([i+1,j])
    answer.sort(key= lambda x:x[1]-x[0])
    return answer[0]