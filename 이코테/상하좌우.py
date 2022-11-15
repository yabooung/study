# 구현 예제4-1 상하좌우 
# 난이도 @00
n = int(input())
plan = input().split()
start = [1,1]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_type = ['U', 'D', 'L', 'R']

for i in plan:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = start[0] + dx[j]
            ny = start[1] + dy[j]
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    start[0] = nx
    start[1] = ny

print(start[0], start[1])
