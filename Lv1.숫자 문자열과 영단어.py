def solution(s):
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] # 알파벳을 모두 입력한 리스트 생성
    for num, alp in enumerate(alpha): # enumerate 함수를 사용해 num이 0일때,alp가 'zero'가 되도록 for문
        if alp in s: #문자열 안에 알파벳이 있다면
            s = s.replace(alp,str(num)) #문자열의 해당 알파벳을 숫자로 치환
    return int(s) # s는 string이니까 integer로 형변환