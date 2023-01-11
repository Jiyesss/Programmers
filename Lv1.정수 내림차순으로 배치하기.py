def solution(n):
    n_sorted = sorted(str(n), reverse = True)
    answer = ''.join(n_sorted)
    return int(answer)