def solution(n):
    numbers = set(range(3,n+1,2)) # n까지의 홀수집합

    for i in range(3,n+1,2): #에라토스테네스의 체 이용
        if i in numbers:
            numbers -= set(j for j in range(2*i, n+1, i))

    return len(numbers) + 1 # 소수 2 포함

'''
def solution(n):
    answer = 1 # 2는 for문에 포함되지 않지만 소수이므로 answer이 1로 시작
    for i in range(3,n+1,2): # 소수= 1과 자기 자신으로만 나누어 떨어짐
        for j in range(2,i): # i라는 수를 2부터 i-1까지 나눴을 때,
            if i % j == 0: # 나누어 떨어지는 수가 있다면 소수가 아님
                break
            elif j == i-1: # 나누어 떨어지는 수가 없다면
                answer += 1 # 소수이므로 answer에 +1
    return answer'''