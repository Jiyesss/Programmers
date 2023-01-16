from itertools import combinations # itertools 모듈 사용
def solution(number):
    count = 0
    combination = list(combinations(number, 3)) # number를 3으로 묶는 모든 조합 생성
    for i in combination: # i는 조합 한 개
        if i[0] + i[1] + i[2] == 0:
            count += 1
    return count