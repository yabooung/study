#월간 코드 챌린지 시즌1
#이진 변환 반복하기
def solution(s):
    count_one = 0
    all_zero = 0

    while True:
        only_one = str(s).count('1')
        count_one += 1
        count_zero = str(s).count('0')
        all_zero += count_zero
        to_bin = bin(only_one)
        s = to_bin[2:]
        print(s)
        if s == '1':
            break
    answer =[count_one, all_zero]

    return answer
