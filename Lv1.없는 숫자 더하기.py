def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return 45-sum