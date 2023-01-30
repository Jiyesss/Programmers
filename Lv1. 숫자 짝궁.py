def solution(X, Y):
    jjak = '-1'
    if set(X)&set(Y): # X랑 Y에 공통 숫자가 있는 경우
        jjak = ''
        for i in range(9,-1,-1): # sort를 쓰면 시간초과가 나니까 9~0까지의 순서
            jjak += str(i) * min(X.count(str(i)),Y.count(str(i)))
        
    return jjak if jjak[0] != '0' else '0' # 공통숫자가 0뿐인 경우도 고려