import heapq as h

def solution(ability, number):
    
    h.heapify(ability)
    
    # 교육 횟수만큼 반복
    for n in range(number):
        # 교육시마다 능력치 제일 안 좋은 직원 2명 뽑기
        education = 0
        education += h.heappop(ability)
        education += h.heappop(ability)
        
        for _ in range(2):
            h.heappush(ability,education)
        
        
        
    return sum(ability)