#1969.DNA
n, m = map(int, input().split())
rotate = [ [] for _ in range(m)]
for i in range(n):
    k = input()
    for j in range(m):
        rotate[j].append(k[j])

answer = ''
word = ['A','C','G','T']
wordans = 0
for i in rotate:
    wordcnt = 0
    bigword = 0
    for j in range(4):
        wordcnt = i.count(word[j])
        if wordcnt > bigword:
            bigword = wordcnt
            wordname = word[j]
    wordans = wordans + n - bigword
    answer += wordname



print(answer)
print(wordans)
