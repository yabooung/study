# dfs
# 재귀 python은 재귀 제한이 있기 때문에 조건 확인

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 기본은 1000
n, m = map(int, input().split())

visited = [0]*(n+1)
graph = [[] for _ in range(n+1) ]
cnt = 0
def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)



for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)


for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
