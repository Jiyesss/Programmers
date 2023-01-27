def solution(k, score):
    answer = []
    honor = [] # 명예의 전당(k번째까지 존재)
    for i in range(len(score)): # 마지막날까지
        if k > len(score): # k가 전체 날짜보다 크면
            honor.append(score[i]) # 명예의 전당에 추가
            honor.sort(reverse = True) # 내림차순 정렬 후
            answer.append(honor[-1]) # 최하위 점수 answer에 추가
        else:
            if i + 1 <= k: # k번째 날까지는
                honor.append(score[i]) # 명예의 전당에 추가
                honor.sort(reverse=True) # 명예의 전당 내림차순 정렬
                answer.append(honor[-1]) #  최하위 점수 answer에 추가
            else: # k번째 날 이후 부터는
                if score[i] > honor[-1]: # 명예의 전당 꼴찌보다 고득점인 경우만
                    honor[-1] = score[i] # 명예의 전당 꼴찌와 교체
                    honor.sort(reverse=True) # 내림차순 정렬
                    answer.append(honor[-1]) # 새롭게 바뀐 최하위 점수 answer에 추가
                else: # 명예의 전당 꼴찌보다 점수가 낮으면
                    answer.append(honor[-1]) # 명예의 전당 꼴찌는 바뀌지 않음

    return answer