# 실전문제 2
# 난이도 1
# 구현

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


k = input()
x = int(k[1])
y = int(ord(k[0])) - int(ord('a')) + 1

cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 8 >= nx > 0 and 8>= ny > 0:
        cnt += 1

print(cnt)
