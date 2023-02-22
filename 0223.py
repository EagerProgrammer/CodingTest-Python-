#https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    dic1 = {} #같은 아이디에 다른 이름이 들어오면 이전에 썼던 이름이 바뀌어야함, Change가 일어났을 때도 바뀌어야함
    # 그래서 고민하다가, dic의 key위에 덮어쓰면 value값이 바뀌는 점을 활용하기로 함
    result = []
    for i in record: #여기서 반복문에서는 dic을 활용해 최종 id에 매핑되는 이름을 정의함
        a = i.split(' ')
        if len(a) == 3:
            dic1[a[1]] = a[2]
    for j in record: #이제 Enter,Leave에 맞는 결과를 추출하기 위한 반복문
        b = j.split(' ')
        aws = ""
        if b[0] == 'Enter':
            aws += dic1[b[1]] + "님이 들어왔습니다."
        elif b[0] == 'Leave':
            aws += dic1[b[1]] + "님이 나갔습니다."
        elif  b[0] == 'Change': #여기서는 아웃풋이 없고 아이디만 바뀌는데 이미 위에서 설정했으므로 continue로 넘어가기
            continue
        result.append(aws) # 이제 하나씩 어펜드하면 끝
    return result