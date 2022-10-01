#연습문제
#다음 큰 숫자
def solution(n):
    k = bin(n).count('1')
    while n <= 1000000:
        n += 1
        ans = bin(n).count('1')
        if ans == k:
            break
    return n
