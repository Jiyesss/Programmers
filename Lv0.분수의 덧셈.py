from math import gcd # 최대공양수 구하는 모듈
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (numer1*denom2) + (numer2*denom1) # 통분하여 계산 한 값의 분자
    denom = denom1 * denom2 # 통분한 분모
    hoho = gcd(numer,denom) # 분자와 분모의 최대공약수
    numer = numer / hoho # 분자를 최대공약수로 나눠줌
    denom = denom / hoho # 분모를 최대공약수로 나눠줌
    answer.extend([numer,denom])
    return answer