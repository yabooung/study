#연습문제
#JadenCase 문자열 만들기
def solution(s):
    s = s.lower()
    temp = list(s)
    
    temp[0] = temp[0].upper()
    for i in range(1,len(temp)):
        if temp[i-1] == ' ':
            temp[i] = temp[i].upper()
    answer = ''.join(temp)
    return answer
    
