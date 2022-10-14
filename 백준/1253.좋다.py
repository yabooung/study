#1253.좋다
#이분검색

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
now = 0
nums.sort()
for i in range(n):
    find = nums[i]
    a = 0
    b = n-1
    while a < b:
        if nums[a] + nums[b] == find:
            if a!=i and b !=i:
                cnt += 1
                break
            elif a == i:
                a+=1
            elif b == i:
                b-=1
        elif nums[a] + nums[b] > find:
            b -= 1
        elif nums[a] + nums[b] < find:
            a += 1
print(cnt)
