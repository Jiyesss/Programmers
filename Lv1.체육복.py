def solution(n, lost, reserve):
    reserve2 = list(set(reserve) - set(lost)) # 새로운 리스트에 넣은 이유는 reserve와 lost에서 모두 중복을 제거하기 위함
    lost2 = list(set(lost) - set(reserve)) # 여벌 가져왔는데 체육복을 도난당한 학생을 reserve와 lost에서 제거
    lost2.sort() # 오름차순 정렬
    reserve2.sort()
    answer = n - len(lost2) # 체육복을 가지고 있는 학생 수
    for i in lost2:
        for j in reserve2:
            if i == j-1 or i == j+1: # 번호가 여분을 가진 학생의 앞 혹은 뒤라면
                answer += 1 # 체육복을 가지고 있는 학생 한 명 추가
                reserve2.remove(j) # 더이상 여벌의 체육복이 없으므로 reserve에서 제거
                break
    return answer