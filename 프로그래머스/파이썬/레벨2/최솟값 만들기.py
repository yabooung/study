#연습문제
#최솟값 만들기
def solution(A,B):
    a = sorted(A)
    b = sorted(B,reverse=True)

    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer
