def solution(x):
    sum = 0
    a = x
    while x >= 10:
        sum += x % 10
        x //= 10
    sum += x
    if a % sum == 0:
        answer = True
    else:
        answer = False
    return answer