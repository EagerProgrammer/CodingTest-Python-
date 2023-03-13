#n이 만약 25로 주어진면 각 숫자에 해당된 알파벳중 하나씩 알파벳을 꺼내서 문자열을 만들고 리턴해준다.(대신 시작은 2부터 시작한다.)
#예를 들어 n이 23이면 [a,b,c] 와 [d,e,f]의 두개의 배열에서 하나씩 골라서 만들수 있는 문자열을 리스트로 반환해준다.
from itertools import product
def solution(n):
    if len(n) == 0:
        return []
    list5 = []
    list1 = list(n)
    list2 = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    list3 = []
    for i in list1:
        i = int(i)
        list3.append(list2[i-2])
    list4 = list(product(*list3))
    for i in list4:
        temp = ''
        for j in i:
            temp += j
            if len(temp) == len(i):
                list5.append(temp)
    return list5
    
