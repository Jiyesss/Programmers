from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion) # Counter 함수를 이용하여 {참가자명:참가자명이 나온 횟수} 를 집계한 후, 참가자-완주자를 해서 완주하지 못한 사람이 answer에 남음
    return list(answer.keys())[0]