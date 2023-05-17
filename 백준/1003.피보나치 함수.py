#1003. 피보나치 함수
# 부분합
# dp
t= int(input())

def fibo(n):

    sum = [0 for _ in range(n)]
    if n == 0:
        return print(1, 0)
    elif n == 1:
        return print(0, 1)
    else:
        sum[0], sum[1] = 1, 1
        for i in range(2,n):
            sum[i] = sum[i-1] + sum[i-2]
        print(sum[-2], sum[-1])




for i in range(t):

    fibo(int(input()))
