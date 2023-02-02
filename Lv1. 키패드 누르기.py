def solution(numbers, hand):
    answer = []
    lh = 10 # '*'
    rh = 12 # '#'
    for num in numbers:
        if num in [1,4,7]: # 1,4,7 의 경우 무조건 왼손
            answer.append('L')
            lh = num
        elif num in [3,6,9]: # 3,6,9의 경우 무조건 오른손
            answer.append('R')
            rh = num
        else:
            if num == 0:
                num = 11 # '0'의 위치
            ld = abs(lh-num)//3 + abs(lh-num) % 3 # 거리 계산
            rd = abs(rh-num)//3 + abs(rh-num) % 3
            if ld < rd:
                answer.append('L')
                lh = num
            elif rd < ld:
                answer.append('R')
                rh = num
            elif rd == ld: # 오른손잡이, 왼손잡이로 구분
                if hand == 'left':
                    answer.append('L')
                    lh = num
                else:
                    answer.append('R')
                    rh = num
    return ''.join(answer)