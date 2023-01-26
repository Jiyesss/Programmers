def solution(lottos, win_nums):
    answer = []
    count = 0 # 일치하는 수의 개수를 세줌
    zero = lottos.count(0) # 0의 개수를 세줌
    for i in lottos:
        for j in win_nums:
            if i == j: # lottos에 들어있는 수랑 win_nums에 들어있는 숫자 같은 경우
                count += 1 # count에 +1 해주기
    if count == 0 and zero == 0: # count도 0이도 zero도 0이면 무조건 낙첨
        answer.extend([6,6]) # append로 두 줄 쓰기 귀찮아서 extend 써줌
    elif count == 0 and zero != 0: # zero가 0이 아닌 경우에는 최고 순위에 변동이 생기므로 경우 추가
        answer.extend([6-zero+1,6])
    else: # 그 외의 경우 최저순위 6에서 count와 zero 개수 빼주고 1더한 값으로 계산
        answer.extend([6-count-zero+1, 6-count+1])
    return answer