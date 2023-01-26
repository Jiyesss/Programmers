def solution(k, m, score): # k는 어디다 쓰는 건지 잘 모르겠네요
    answer = 0
    score = sorted(score, reverse = True) # score 내림차순 정렬
    for i in range(1, len(score)//m + 1): # 상자의 개수
        answer += score[m*i-1] * m # 각 상자에 마지막 사과(=최저 점수) * 한사과당 사과 개수
    return answer