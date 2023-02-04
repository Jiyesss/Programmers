def solution(board, moves):
    answer = 0
    loc = 0 # 인형뽑을 위치
    baguni = [] # 인형이 담긴 바구니
    for i in range(len(moves)):
        loc = moves[i] - 1
        for j in board: # 인형을 바구니에 넣고 board에서 제거
            if j[loc] != 0:
                baguni.append(j[loc])
                j[loc] = 0
                break
        if len(baguni) >= 2: # 같은 종류의 인형이 두개가 연속이면 제거
            if baguni[-1] == baguni[-2]:
                baguni.pop()
                baguni.pop()
                answer += 2
    return answer