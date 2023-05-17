#10986.나머지 합
#부분합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0] * (n+1)
cnt = [0]*m
answer = 0

for i in range(n):
    sums[i] = sums[i-1]+nums[i]

    temp = sums[i] % m
    if temp == 0:
        answer += 1
    cnt[temp] += 1

for i in range(m):
    if cnt[i] > 1:
        answer += cnt[i] * (cnt[i]-1) // 2


print(answer)
