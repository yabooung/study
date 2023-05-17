# 2018.수들의 합 5.py
# 투 포인트

n = int(input())
start =1
end = 1
sum = 1
count = 1
while end != n:
    if sum == n:
        count+=1
        end += 1
        sum += end
    elif sum > n :
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)
