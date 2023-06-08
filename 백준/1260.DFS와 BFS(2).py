#1260.DFS와 BFS

from collections import deque
n, m, s = map(int, input().split())

graph = [ [] for _ in range(n+1)]
visit_dfs = [False] *(n+1)
visit_bfs = [False] *(n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    print(now, end=" ")
    visit_dfs[now] = True
    for i in graph[now]:
        if not visit_dfs[i]:
            dfs(i)

def bfs(now):
    que = deque()
    que.append(now)
    visit_bfs[now] = True
    while que:
        que_now = que.popleft()
        print(que_now, end=" ")
        for i in graph[que_now]:
            if not visit_bfs[i]:
                visit_bfs[i]= True
                que.append(i)
for i in graph:
    i.sort()

dfs(s)
print()
bfs(s)

