n = int(input())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

result = 0
for i in range(n):
    a = max(lista)
    a_index = lista.index(a)
    lista.pop(a_index)
    b = min(listb)
    b_index = listb.index(b)
    listb.pop(b_index)
    result = result + (a*b)
print(result)
