def solution(t, p):
    answer = 0
    tlist = [] # t에서 p와 길이가 같은 부분문자열 리스트
    for i in range(len(t)-len(p)+1):
        tlist.append(t[i:i+len(p)]) # tlist에 부분문자열 추가
    for j in tlist: # tlist 안의 수가 p보다 작거나 같으면!
        if j <= p:
            answer += 1 # answer에 +1
    return answer