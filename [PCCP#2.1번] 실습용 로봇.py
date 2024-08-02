def solution(command):
    answer = [0,0]
    # 0: 정면, 1: 우측. 2: 후면, 3: 좌측
    direct = 0
    for c in command:
        if c == 'R':
            if direct + 1 < 4:
                direct += 1
            else:
                direct = 0
        elif c == 'L':
            if direct - 1 >= 0:
                direct -= 1
            else:
                direct = 3
        
        elif c == 'G':
            if direct == 0:
                answer[1] += 1
            elif direct == 1:
                answer[0] += 1
            elif direct == 2:
                answer[1] -= 1
            else:
                answer[0] -= 1
        else:
            if direct == 0:
                answer[1] -= 1
            elif direct == 1:
                answer[0] -= 1
            elif direct == 2:
                answer[1] += 1
            else:
                answer[0] += 1
        
    return answer