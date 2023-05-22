#https://school.programmers.co.kr/learn/courses/30/lessons/42579
#list를 돌면서 곡의 종류와 그 종류에 해당하는 인덱스 그리고 총합까지 알아야했다.
#그래서 dict 두개로 분리하여 하나는 총합 하나는 인덱스와 곡수를 기록시킨후에
#sort 조건들을 맞춰서 answer에 넣어주었다. 이 때 길이가 1일 수도 있어서 테케 예외처리로 1일때를 추가해줘야 만점이 나옵니다.
def solution(genres, plays):
    dic = {}
    dic1 = {}
    answer = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], []) + [[plays[i],i]]
    for j in range(len(genres)):
        dic1[genres[j]] = dic1.get(genres[j],0) + plays[j]
    dic1 = sorted(dic1.items(), key = lambda item: item[1], reverse = True)
    for i in dic1:
        temp = dic[i[0]]
        temp.sort(key=lambda x:x[0], reverse=True)
        if len(temp) ==1:
            for j in range(1):
                answer.append(temp[j][1])
        else:
            for j in range(2):
                answer.append(temp[j][1])
    return answer