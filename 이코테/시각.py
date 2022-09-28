# 구현 4-2
# 시각

n = int(input())
cnt = 0
for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            sum = str(hour)+str(min)+str(sec)
            print(sum, sum.count('3'))
            if sum.count('3') >= 1:
                cnt += 1

print(n, cnt)
