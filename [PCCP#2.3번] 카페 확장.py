from collections import deque

def solution(menu, order, k):
    max_customer = 0
    current_customer = 0
    make_times = deque()  # 음료가 완성되는 시간을 저장하는 큐
    time = 0

    for i in range(len(order)):
        arrival_time = i * k

        # 도착한 손님이 현재 시각보다 크면 현재 시각을 도착 시각으로 맞춘다
        if time < arrival_time:
            time = arrival_time

        # 현재 시각에 도착한 손님이 있다면 큐에서 음료가 완성되는 시간을 계산
        while make_times and make_times[0] <= time:
            make_times.popleft()
            current_customer -= 1

        # 새로 도착한 손님에 대해 음료 완성 시간을 큐에 추가
        finish_time = time + menu[order[i]]
        make_times.append(finish_time)
        current_customer += 1

        # 최대 손님 수 갱신
        if current_customer > max_customer:
            max_customer = current_customer

        # 다음 손님 도착까지의 시간 증가
        time += menu[order[i]]

    return max_customer

# 테스트 케이스
print(solution([5, 12, 30], [1, 2, 0, 1], 10))  # 3
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))  # 4
print(solution([5], [0, 0, 0, 0, 0], 5))  # 1
print(solution([2, 3], [0, 1, 0, 1, 0, 1], 2))  # 2