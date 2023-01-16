def solution(n):
    answer = 0
    result = ''
    while n > 0:
        answer = str(n % 3)
        n //= 3
        result += answer
    return int(result,3)