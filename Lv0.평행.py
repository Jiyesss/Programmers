from itertools import combinations
def solution(dots):
    answer = []
    dap = 0
    for i in combinations(dots,2):
            scope = (i[1][1]-i[0][1]) / (i[1][0]-i[0][0]) # 기울기 구하는 공식 y증가량/x증가량 아시죠?
            if scope in answer: # 기울기가 같다면 1 출력
                dap = 1
                break
            else:
                answer.append(scope)
    return dap