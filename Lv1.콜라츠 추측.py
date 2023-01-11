def solution(num):
    count = 0
    if num == 1:
        count = 0
    elif num > 1:
        while count < 500 and num != 1:
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                num = (num*3) +1
                count += 1
        if count >= 500:
            count = -1
    return count