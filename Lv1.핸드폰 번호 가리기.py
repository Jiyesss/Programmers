def solution(phone_number):
    l_phone_number = list(phone_number)
    for i in range(len(l_phone_number)-4):
        l_phone_number[i] = '*'
    answer = "".join(l_phone_number)
    return answer