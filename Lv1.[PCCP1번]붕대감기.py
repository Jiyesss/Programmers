def solution(bandage, health, attacks):
    answer = health
    healing = 0
    index = 0
    for i in range(attacks[-1][0]+1): # 마지막 최종 공격시간 까지
        
        # 1)공격 당했을 때
        if (i == attacks[index][0] and index < len(attacks)): # 공격 당한 시간이면
            if (answer - attacks[index][1] <= 0): # 체력이 0이 되면 즉시 종료
                return -1
            else: 
                answer -= attacks[index][1] # 공격만큼 체력 깎고
                index += 1
                healing = 0
            
        # 2) 공격 안 당했을 때
        else:
            healing += 1 # 힐링 시전시간 증가
            
            if (healing == bandage[0]): # 시전시간 다 찼으면
                if (answer + bandage[2] + bandage[1] <= health): # 최대체력 못넘김
                    answer += bandage[2] + bandage[1]
                else:
                    answer = health
                healing = 0 # 연속시전시간 초기화
            else: # 시전시간 안찼으면
                if (answer + bandage[1] <= health): # 최대체력 안 넘기면
                    answer += bandage[1] # 힐해주기
                else: 
                    answer = health # 최대체력으로
                
            
    if (answer <= 0):
        return -1
    else:
        return answer
        
        
    