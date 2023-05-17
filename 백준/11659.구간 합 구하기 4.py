#11659.구간 합 구하기 4.py
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0]*(n+1)

for i in range(len(nums)):
        sum[i+1] = (nums[i]+sum[i])

for i in range(m):
    start, end = map(int, input().split())
    print(sum[end]-sum[start-1])
