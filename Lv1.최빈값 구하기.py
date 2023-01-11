def solution(array):
    answer = {}
    for i in array:
        if i in answer:
            answer[i] += 1
        else: 
            answer[i] = 1
    sorted_answer = sorted(answer.items(), reverse = True,key = lambda item:item[1])
    if len(sorted_answer) <= 1:
        mode = sorted_answer[0][0]
    else:
        if sorted_answer[0][1] == sorted_answer[1][1]:
            mode = -1
        else:
            mode = sorted_answer[0][0]
    return mode