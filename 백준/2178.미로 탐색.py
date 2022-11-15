#2178 미로탐색
#bfs

from collections import deque

def bfs(x,y):
    que = deque()
    que.append([x,y])
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] +x
            ny = dy[i] +y

            if nx < 0 or ny <0 or nx>= n or ny >=m:
                continue
            else:
                if miro[nx][ny] == 0:
                    continue
                if miro[nx][ny] ==1:
                    miro[nx][ny] = miro[x][y]+1
                    que.append([nx,ny])
    return miro[n-1][m-1]

print(bfs(0,0))
