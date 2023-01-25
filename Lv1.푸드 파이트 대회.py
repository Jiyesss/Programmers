def solution(food):
    answer, reverse = '', '' # answer, reverse 문자열 생성
    for i in range(1,len(food)): # 1부터 시작해서 물 제거
        answer += str(i) * (food[i]//2) # //로 음식의 개수가 홀수인 경우 고려
    reverse = answer[::-1] # reverse안에 answer를 뒤집어서 넣어주기
    answer += '0'
    return (answer + reverse)