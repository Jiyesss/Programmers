from itertools import combinations # 조합 모듈 사용
def solution(nums):
    answer = 0
    prime = []
    comb = combinations(nums,3) # nums 안에서 3개 뽑아줌(조합으로)
    for i in comb:
        prime.append(sum(i)) # 3개를 골라서 더함
    for j in prime: # prime 안의 중복 제거 안 하니까 되네?
        for k in range(2,j): # 소수 판별
            if j % k == 0:
                break
            elif k == j-1:
                answer += 1
    return answer