#https://school.programmers.co.kr/learn/courses/30/lessons/42883
#계속 max empty에러가 뜬다 인덱스 설정에 문제가 있는것 같다. 다시 찾아서 해결해야한다.
def solution(number, k):
    answer = ''
    x = len(number)-k
    for i in range(x):
        y = -x+i+1
        if len(answer) == x:
            break
        elif y == 0:
            a = max(number[i:])
            answer += a
            print(answer)
        elif y != 0 and i != (-y+len(number)):
            a = max(number[i:y])
            answer += a
            number = number.replace(a,'')
            print(answer)
    return answer
# 답안
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0: #이 조건을 생각해낸게 대단하네, 하나씩 걸러내면서, k를 줄여가서 자리수 만큼만 꼐산하게 한다. 그리고 stack에 결과를 넣고 뺴고 반복
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)