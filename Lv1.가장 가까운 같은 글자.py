def solution(s):
    answer = []
    dict = {} # 딕셔너리 생성
    for idx, i in enumerate(s): # enumerate함수 사용하여 문자열 인덱스 보여주기
        if i in dict: # 딕셔너리에 해당 문자가 있다면
            answer.append(idx-dict[i]) # 해당 문자열의 인덱스에서 딕셔너리의 value값(자신보다 앞에 있는 같은 글자의 인덱스)빼기 
            dict[i] = idx # 딕셔너리의 인덱스 업데이트해주기
        else:
            answer.append(-1)
            dict[i] = idx
    return answer