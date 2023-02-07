#https://school.programmers.co.kr/learn/courses/30/lessons/60057
#2020 카카오 공채 1번문제(정답률 28%로) 1번문젝 이게 맞나 싶다. 근데 사실 조금만 생각하면 풀만한긴한데....모르겠다..존나 어렵네
def solution(s):
    if len(s) == 1: # 길이가 1인 경우를 고려안하면 테스트 케이스에서 한문제 계속에러뜬다. 이거 고민하다가 시간날린다.
        ans = 1
    answer = []
    for n in range(1,len(s)):
        y = [s[i:i+n] for i in range(0,len(s),n)] # list comphersion으로 주어진 s를 n까지 크기를 가지는걸로 등분 가능하다.
        result = '' #우리의 최종결과 문자열 담기
        k = '' #비교하는 대상을 담기
        count = 0 #비교하는 문자열이 뒤에랑 몇개 일치하는지 체크
        for j in y:
            if len(k) == 0: #처음에 k에 첫 문자열을 넣기 위해
                k = j 
                count += 1  #자기 자신이 이미 하나존재하니까 카운트 1개
            elif len(k) > 0 and k == j: #이미 한개 존재하면서 뒤에 문자열과 비교 시작 그리고 만약 같다면 카운트만 증가
                count += 1 
            elif len(k) > 0 and k != j: #뒤에 문장과 달라지는 순간이오면 우리는 result에 업데이트 해줘야한다.
                if count > 1: # 이제 1보다 크다면 우리는 숫자와 함께 문자열을 결과에 기입해준다.
                    result += str(count) + k 
                else: #하지만 자기 자신만 같을 때는 1을 생략하기로 했으므로 문자열만 넣어준다.
                    result += k
                count = 1 #이제 비교가 끝나고 현재 받은 j로 다음 문자열과 비교해줘야하므로 다시 셋팅하는 구간이다.
                k = j
        # 밑에 조건문을 안해주면 마지막 비교해주는 문자열들은 result에 업데이트가 안된다 그래서 이 부분이 필요함       
        if count > 1:            
            result+=str(count)+k          
        else:
            result+=k
        answer.append(len(result)) # 이제 각 결과들을 리스트에 답는다
        ans = min(answer)  #이제 이중에 가장 적은 수를 가진 결과를 반홚한다.
        
    return ans