def solution(a, b):
    answer = 0
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31] # 월 별로 일수 세기
    for i in range(a-1): # 해당 월까지의 일수를 계산
        answer += day[i] 
    answer += b # 해당 일을 더하기
    
    return week[(answer+4) % 7] # 1월 1일 기준 금요일이므로 인덱스 맞춰서 나머지 구함