# 그리디 3.숫자 카드 게임

n, m = map(int, input().split())

answer = 0
for i in range(n):
    cards = list(map(int,input().split()))
    x = min(cards)
    if answer < x:
        answer = x
print(answer)
