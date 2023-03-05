#https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = []
    count = 0
    count1 = 0
    while len(s) != 1: #길이가 1이 아니면 계속해서 반복문 돌게하기
        a = s.count('0') #0의 개수 세기
        b = len(s) - a #0을 제거한 후 길이
        if b == 0:
            break
        else:
            s = bin(b)[2:] #2진 변환 후 앞에 0b제거
            count += 1 #몇번 이진으로 변환했는지
            count1 += a #몇개의 0을 제거했는지
    answer.append(count)
    answer.append(count1)
    return answer