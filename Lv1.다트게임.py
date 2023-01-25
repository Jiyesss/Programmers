def solution(dartResult):
    score = '' # 3번의 점수를 각각 담을 문자열 score
    answer = []
    for i in dartResult:
        if i.isdigit(): # 숫자인 경우, 문자열에 추가
            score += i # 만약 score 형태가 integer이면, 10이 1과 0으로 따로 계산됨
        elif i == 'S': # S,D,T를 다 if문으로 경우 나눔
            score = int(score) # single 은 점수변화 없음
            answer.append(int(score)) # answer 리스트에 score 값 추가
            score = '' # score는 한 차례 지나갈 때마다 초기화
        elif i == 'D':
            score = int(score) ** 2 # double 점수 제곱
            answer.append(int(score))
            score = ''
        elif i == 'T': # triple 점수 세제곱
            score = int(score) ** 3
            answer.append(int(score))
            score = ''
        elif i == '*':
            if len(answer) <= 1: # *이 첫 차례에 등장했을 경우
                answer[-1] *= 2 # 첫번째 점수만 두 배
            elif len(answer) > 1: # *이 두번째 혹 세번째이면
                answer[-1] *= 2 # 해당 차례의 점수와
                answer[-2] *= 2 # 그 전 차례의 점수도 두배
        elif i == '#':
            answer[-1] *= -1 # *과 중첩되는 경우도 고려
    return sum(answer)