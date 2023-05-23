#골드4
#17298.오큰수.py
#스택

n = int(input())
number = list(map(int, input().split()))

answer = [0] * n
stack = []
for i in range(n):
    while stack and number[stack[-1]]<number[i]:
        answer[stack.pop()] = number[i]
    stack.append(i)
while stack:
    answer[stack.pop()] = -1

for i in answer:
    print(i, end=" ")
