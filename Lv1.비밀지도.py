def solution(n, arr1, arr2):

    bin1 = []
    bin2 = []
    answer = []

    for i in range(n): #10진수 2진수 변환
        bin1.append(format(arr1[i],'b').zfill(n))
        bin2.append(format(arr2[i],'b').zfill(n))

    for i,j in zip(bin1,bin2): #arr1과 arr2의 첫번째줄부터 하나씩 인덱싱함
        answer_1col = ''
        for k in range(n):
            if i[k] == '0' and j[k] == '0':
                answer_1col += ' '
            else:
                answer_1col += '#'
        answer.append(answer_1col)

    return answer
