def solution(array, commands):
    answer = []
    for i in commands:
        cut = [] # cut은 for문 돌 때마다 초기화
        cut = array[i[0]-1:i[1]] # commands의 i번째부터 j부터까지의 원소 슬라이싱
        cut.sort() # 인덱싱한 원소를 오름차순 정렬
        answer.append(cut[i[2]-1]) # answer에 cut의 k번째 원소 추가
    return answer