def solution(sizes):
    max_w = 0
    max_h = 0
    for i in sizes:
        if i[0] < i[1]:
            i.reverse()
        max_w = max(max_w,i[0])
        max_h = max(max_h,i[1])
    return max_w * max_h