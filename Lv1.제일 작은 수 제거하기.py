def solution(arr):
    if len(arr) == 0 or len(arr) == 1:
        arr[0] = -1
    else:
        min_arr =min(arr)
        arr.remove(min_arr)
    return arr