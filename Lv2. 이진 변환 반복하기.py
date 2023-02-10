def solution(s):
    answer = []
    zcount = 0 # zero 개수 
    count = 0 # 이진 변환 횟수
    while s != '1': # s가 1이 될 때까지 반복
        # s에서 zero의 갯수를 세고, s에서 0을 제거함
        zcount += s.count('0')
        s = s.replace('0','')
        # s 이진 변환
        s = bin(len(s))[2:]
        count += 1
    answer.append(count)
    answer.append(zcount)
    return answer