from collections import Counter
def solution(k, tangerine):
    result = Counter(tangerine) #리스트 안에서 같은 인덱스를 체크하기 위해 Counter 함수 사용 일반적인 count보다 시간복잡도가 더 좋다
    c = result.values() #values값만 가져오기
    c = sorted(c, reverse = True)#values 값을 가져와서 내림차순으로 정렬
    idx = 0
    count = 0
    while k > 0:
        k = k -c[idx] #가져온 vlaues값을 순회하면서 k보다 크거나 같게 만드는 조건 설정 그리고 k에서 지속적으로 빼주면서 0이거나 0보다 작으면 탈출
        count += 1 #동시에 카운팅(이게 숫자의 종류를 파악하는 카운팅)
        idx += 1 #인덱스를 넘어가면서 k를 0보다 작거나 0과 같게 만든다
    return count