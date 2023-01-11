def solution(n):
    answer = []
    n_str = str(n)
    for i in range(len(n_str)):
        answer.append(int(n_str[len(n_str)-(i+1)]))
    return answer