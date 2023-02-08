from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    alphabet = list(ascii_lowercase)

    for i in skip:
        alphabet.remove(i)
    alphabet = alphabet * 3 # z에서 a로 보내는 거
    for j in s:
        answer += alphabet[alphabet.index(j) + index]
        
    return answer