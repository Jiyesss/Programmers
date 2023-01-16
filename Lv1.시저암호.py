def solution(s, n):
    answer = ''
    alpha_list = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i.islower():
            answer +=alpha_list[(alpha.find(i)+n) % 26]
        elif i.isupper():
            answer +=alpha_list[(alpha.find(i.lower())+n) % 26].upper()
        elif i == ' ':
            answer += i
    return answer