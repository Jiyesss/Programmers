def solution(n, m):
    answer = []
    for i in range(1, min(n,m)+1): #최대공약수 구하기
        if n % i == 0 and m % i == 0:
            gcd = i
    for i in range(max(n,m),n*m+1): #최소공배수 구하기
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    answer.append(gcd) 
    answer.append(lcm)
    return answer