#2164. 카드2
#큐

from collections import deque
n = int(input())
card = deque()
for i in range(1,n+1):
    card.append(i)

while card:
    if len(card) == 1:
        break
    j = card.popleft()
    k = card.popleft()
    card.append(k)


print(card.pop())
