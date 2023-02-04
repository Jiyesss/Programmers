def solution(s):
    answer = 0
    count = 0
    while len(s) > 0:  # s의 길이가 0이 될 때까지
        for i in range(len(s)):
            x = s[0]  # s의 첫 번째 글자
            if s[i] == x:  # x와 같으면 +1
                count += 1
            else:  # x와 다르면 -1
                count -= 1
            if count == 0 or i == len(s) - 1:  # 0이 될 때마다 문자열 슬라이싱 혹은 끝까지 다 돌았으면 슬라이싱
                s = s[i + 1:]
                answer += 1
                break

    return answer