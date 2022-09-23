#연습문제
#숫자의 표현
def solution(n):
    if n == 1:
        return 1
    k = n // 2
    if n % 2 == 1:
        k+=1
    answer = 0
    for i in range(k):
        start = i+1
        count = 0
        for j in range(start, k+1):
            count += j
            if count > n:
                break
            if count == n:
                answer += 1
                break
        
    return answer+1
