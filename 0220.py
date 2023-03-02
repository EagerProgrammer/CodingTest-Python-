#https://school.programmers.co.kr/learn/courses/30/lessons/12909
#올바른 괄호로이루어진 배열 찾기 stack을 활용해서 풀었다.
def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True