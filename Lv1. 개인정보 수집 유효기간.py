def solution(today, terms, privacies):
    answer = []
    # terms를 딕셔너리로 (약관종류):(약관기한) 만들어줌
    terms = {i.split()[0]:int(i.split()[1])*28 for i in terms}
    # today도 년 월 일을 모두 더해 일로 바꿔줌
    year,month,day = today.split('.')
    today = (int(year)*12*28) + (int(month)*28) + (int(day))
    # privacies 에 있는 날짜도 일단위로 바꾸고, yak에 약관 종류를 넣어줌
    for num,i in enumerate(privacies):
        year,month,day = i.split()[0].split('.')
        yak = i.split()[1]
        i = (int(year)*12*28) + (int(month)*28) + (int(day))
        # 약관 유효기간 + 개인정보 수집일자가 오늘 날짜를 지났다면
        if today >= terms[yak] + i:
            # answer에 num+1 추가해주기
            answer.append(num+1)

    return answer