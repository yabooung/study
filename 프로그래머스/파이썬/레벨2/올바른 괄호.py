#스택/큐
#올바른 괄호
from collections import deque
def solution(s):
    answer = 0
    que = deque(s)
    while que:
        k = que.popleft()
        if answer == -1:
            return False
        if k == '(':
            answer += 1
        else:
            answer -= 1
            
    if answer == 0:
        return True
    else:
        return False
