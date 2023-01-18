def solution(nums):
    pocketmon = int(len(nums)/2) # pocketmon안에 nums/2 넣어줌
    if len(set(nums)) < len(nums)/2: # 포켓몬의 종류가 nums/2보다 작으면,
        return len(set(nums)) # 포켓몬의 종류가 정답
    else:
        return len(nums)/2 # 아니면, nums/2 가 정답
'''
from itertools import combinations  # 조합 모듈 사용
def solution(nums):
    pocketmonmon = []
    pocketmon = set(combinations(nums, int(len(nums) / 2))) # 가능한 조합을 set으로 만들어서 중복 제거
    answer = 0
    for i in pocketmon:
        pocketmonmon.append(set(i)) # set으로 만들어서 중복 포켓몬 제거
    for j in pocketmonmon:  # 조합에 들어있는 포켓몬의 종류가 많은 경우
        if len(j) > answer:
            answer = len(j) # answer에 추가
    return answer
'''