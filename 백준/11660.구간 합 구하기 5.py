#11660.구간 합 구하기 5
#구간합 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

maps = [list(map(int, input().split()))  for _ in range(n)]
sums = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + maps[i-1][j-1]

for i in range(m):
    answer = list(map(int,input().split()))
    result = sums[answer[2]][answer[3]] - sums[answer[0]-1][answer[3]] -sums[answer[2]][answer[1]-1] + sums[answer[0]-1][answer[1]-1]



    print(result)
