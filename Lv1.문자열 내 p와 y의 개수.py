def solution(s):
    pSum = 0
    ySum = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            pSum += 1
        elif s[i] == 'y':
            ySum += 1
        else:
            continue
    if pSum != ySum:
        return False
    else:
        return True