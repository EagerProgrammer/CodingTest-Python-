#https://school.programmers.co.kr/learn/courses/30/lessons/43165
#DFS,BFS 문제로 볼수도 있지만 단순 반복문의 알고리즘만 구상해도 풀 수 있다.
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer