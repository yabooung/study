#13023. ABCDE
#DFS

n, m = map(int, input().split())

lst = [[] for _ in range(n)]
visit = [False] * n
arrive = False
for i in range(m):
    a,b = map(int, input().split())

    lst[a].append(b)
    lst[b].append(a)

def dfs(now,depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visit[now] = True
    for i in lst[now]:
        if not visit[i]:
            dfs(i,depth+1)
    visit[now] = False

for i in range(n):
    dfs(i,1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)
