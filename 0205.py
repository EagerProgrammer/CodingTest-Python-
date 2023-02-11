def solution(numbers):
    compare = []
    result = [-1]*len(numbers)
    for i in range(len(numbers)):
        while compare and compare[-1] < numbers[i]:
            result[i] = numbers[i]
        compare.append(numbers[i])
    return compare
#틀린 코드 근데 해답을 봐도 모르겠다....물어봐야겠다 내일랴