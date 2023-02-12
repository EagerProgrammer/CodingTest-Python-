#https://school.programmers.co.kr/learn/courses/30/lessons/1845
#set에 대한 이해만 있으면 정말 쉽게 풀린다.(중복제게)
def solution(nums):
    answer = 0
    num = set(nums)
    k = len(nums)//2
    if len(num) < k:
        answer = len(num)
    else:
        answer = k
    return answer