def solution(a, b, n):
    answer = 0
    while n >= a: 
        answer += (n//a) * b # n/a의 몫 x b 의 값을 더해줌
        n = (n//a) * b + (n%a) # answer에 그 나머지 값을 더한 값이 다음 n
    return answer