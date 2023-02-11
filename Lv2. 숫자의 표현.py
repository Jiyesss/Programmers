def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n: # 합계가 n이 되면 answer +1
                answer += 1
                break
            elif sum > n: # 합계가 n을 넘어가면 break
                break
    return answer