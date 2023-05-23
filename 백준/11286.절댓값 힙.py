#실버1
#11286.절댓값 힙
#우선순위 큐

import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
que = PriorityQueue()

for i in range(n):
    k = int(input())
    if k == 0:
        if que.empty():
            print(0)
        else:
            ans = que.get()
            print(ans[1])
    else:
        que.put((abs(k),k))

