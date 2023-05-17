#1940.주몽
#투포인터
n = int(input())
m = int(input())

score = list(map(int,input().split()))
score.sort()

start = 0
end = n - 1

cnt = 0
while start < end:
    if score[start] + score[end] > m:
        end -=1
    elif score[start] + score[end] < m:
        start += 1
    else:
        cnt +=1
        start += 1
        end -=1

print(cnt)
