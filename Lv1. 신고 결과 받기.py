def solution(id_list, report, k):
    answer = []
    report = set(report) # 중복 제거
    id_dict = {i:0 for i in id_list} # 아이디 별로 신고 당한 횟수 적을 딕셔너리
    singo = []
    for i in report: # 각 아이디 별 신고 당한 횟수 집계
        id_dict[i.split()[1]] += 1
    for key in id_dict: # k번을 넘지 않았으면, 정지를 먹지 않음
        if id_dict[key] >= k:
            singo.append(key) # singo에 정지 먹은 유저만 추가

    report = [i.split()[0] for i in report if i.split()[1] in singo] # report에 신고당한 이용자가 정지먹은 신고자만 남김
    for m in id_list:
        answer.append(report.count(m))


    #print(answer)
    return answer