def solution(number, limit, power):
    count = []  # 약수의 개수를 담음
    for i in range(1, number + 1):  # 1단계: 약수의 개수 세기
        a = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j== 0:
                a += 1
                if i ** (1 / 2) != j:
                    a += 1
        count.append(a)
    for k in range(len(count)):  # 2단계: limit 을 초과하는 경우 기본 power 설정
        if count[k] > limit:
            count[k] = power
    return sum(count)  # 철의 무게 구하기