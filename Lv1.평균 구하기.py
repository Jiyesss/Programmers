def solution(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    answer = 0
    answer =sum/len(arr)
    return answer