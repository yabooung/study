#12891. DNA 비밀번호
#슬라이딩 윈도우
#문자열

s, p = map(int, input().split())
letter = input()
answer = list(map(int, input().split()))
start = letter[0:p]
now = [0] * 4
count = 0
checklist = 0

for i in range(4):
    if answer[i] == 0:
        checklist += 1
for i in start:
    if i == 'A':
        now[0] += 1
        if now[0] == answer[0]:
            checklist +=1
    if i == 'C':
        now[1] += 1
        if now[1] == answer[1]:
            checklist +=1
    if i == 'G':
        now[2] += 1
        if now[2] == answer[2]:
            checklist +=1
    if i == 'T':
        now[3] += 1
        if now[3] == answer[3]:
            checklist +=1
if checklist == 4:
    count += 1


for i in range(p, s):
    j = i - p

    if letter[i] == 'A':
        now[0] += 1
        if now[0] == answer[0]:
            checklist +=1
    if letter[i] == 'C':
        now[1] += 1
        if now[1] == answer[1]:
            checklist +=1
    if letter[i] == 'G':
        now[2] += 1
        if now[2] == answer[2]:
            checklist +=1
    if letter[i] == 'T':
        now[3] += 1
        if now[3] == answer[3]:
            checklist +=1

    if letter[j] == 'A':
        if now[0] == answer[0]:
            checklist -=1
        now[0] -= 1
    if letter[j]== 'C':
        if now[1] == answer[1]:
            checklist -=1
        now[1] -= 1
    if letter[j] == 'G':
        if now[2] == answer[2]:
            checklist -=1
        now[2] -= 1
    if letter[j] == 'T':
        if now[3] == answer[3]:
            checklist -=1
        now[3] -= 1
    if checklist == 4:
        count += 1


print(count)
