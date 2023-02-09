def solution(s):
    answer = 0
    if not s[0] == '(' or not s[-1] == ')': # 시작과 끝이 각각 '('.')'가 아니면 false
        return False
    for i in s:
        if i == '(':
            answer += 1
        else:
            answer -= 1
            if answer < 0: # '('보다 ')'가 더 많아지면 무조건 false
                return False
    if answer == 0:
        return True
    
    return False