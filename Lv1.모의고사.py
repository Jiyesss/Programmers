def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5] # 수포자의 찍는 방식을 만들어줌
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0] # 각 수포자의 점수는 0점에서 시작
    for i,j in enumerate(answers): # enumerate 활용해서
        if j == supo1[i % len(supo1)]:# 각 수포자의 점수를 구함
            score[0] += 1
        if j == supo2[i % len(supo2)]:
            score[1] += 1
        if j == supo3[i % len(supo3)]:
            score[2] += 1
    winner = max(score) # winner라는 변수에 가장 높은 점수를 넣어줌
    for i in range(len(score)): # 수포자들 중, 가장 높은 점수를 가진 사람이
        if score[i] == winner: # winner가 된다.
            answer.append(i+1)
    return answer