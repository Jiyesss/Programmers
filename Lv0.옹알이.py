def solution(babbling):
    baby = ['aya','ye','woo','ma']
    for i in baby:
        for j,k in enumerate(babbling):
            if i in k:
                babbling[j] = k.replace(i,'1')
    for i,k in enumerate(babbling):
        babbling[i] = k.replace('1','')
    answer = babbling.count('')
    return answer