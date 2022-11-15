k = int(input())
cnt = 0
n = 1
while True:
    n = n + (6 * cnt)
    cnt = cnt + 1
    if k <= n:
        break
print(cnt)
