#연습문제
#최댓값과 최솟값
def solution(s):
    temp = list(map(int, s.split(' ')))
    big = max(temp)
    small = min(temp)

    answer = f'{small} {big}'
    
    return answer
