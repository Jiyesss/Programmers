def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    for i in new_id: # 2단계
        if i.isdigit() or i.isalpha() or i in ['-','_','.']:
            answer += i
    while '..' in answer: # 3단계
        answer = answer.replace('..','.')
    answer = answer.strip('.') # 4단계
    if not answer: # 5단계
        answer = 'a'
    if len(answer) >= 16: # 6단계
        answer = answer[:15]
        answer = answer.rstrip('.')
    if len(answer) <= 2: # 7단계
        last = answer[-1]
        while len(answer) < 3:
            answer += last  
    return answer