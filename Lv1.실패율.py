def solution(N, stages):
    answer = []
    level = len(stages)
    for i in range(1, N+1):
        if level == 0: # N이 0인 경우
            fail = 0
        else:
            fail = stages.count(i) / level # 실패율 계산
        answer.append([i, fail])
        level -= stages.count(i)
    answer = sorted(answer, key=lambda x:x[1], reverse=True) # 실패율 기준 내림차순 정렬
    answer = [i[0] for i in answer]
    return answer