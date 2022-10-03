#완전탐색
#카펫

def solution(brown, yellow):
    nemo = brown + yellow

    a = 3
    answer=[]
    while True:
        b = nemo // a
        if b < 3:
            continue
        else:
            if brown == 2*(a+b)-4 and a*b == nemo:
                return [b,a]
                break
        a += 1
