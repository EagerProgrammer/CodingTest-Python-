#https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 맨처음 풀이 방식 : 이진법이기에 한 자리 더 큰 만큼까지 for문으로 +1 씩하면서 1 or 2만큼 다른 비트를 찾아서 넣어줬다.
# 테스트 9,10에서 시간초과가 뜬다
def solution(numbers):
    result = []
    for i in numbers:
        x = bin(i)[2:]
        for j in range(1,2**(len(x)+1) - 2**(len(x))):
            count = 0
            y = bin(i+j)[2:]
            if len(x) < len(y):
                x = "0" + x
            for a in range(len(x)):
                if x[a] != y[a]:
                    count += 1
            if count == 1 or count == 2:
                result.append(i+j)
                break
    return result
# 힌트 보고 푼것
# 짝수는 걍 1만 더해주면 그게 답이고
# 홀수는 뒤에서부터 0을 찾아오면서 그것을 1로 바꾸고 바로 옆에 인덱스를 1로 바꾸면 그게 답이다.
# 그래서 bin으로 받은 문자열을 다시 list 로 쪼개고 rfind를 찾은 지점 바로 옆 인덱스르 0으로 바꿔주면 된다.
def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer