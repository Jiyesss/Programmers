from itertools import combinations # itertools 조합 사용
def solution(numbers):
    answer = []
    for i in combinations(numbers, 2): # numbers에서 조합으로 2개 뽑기
        answer.append(sum(i)) # answer에 2개 값의 합 추가
    return list(sorted(set(answer))) # answer에서 set으로 바꿔 중복 제거후 오름차순하고 리스트화