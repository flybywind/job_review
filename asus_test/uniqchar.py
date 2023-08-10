import math
'''
Pay attention, if N is prime number and bigger than 26, the result string len 
will be not equal to N . 
'''
def solution(N):
    d = "abcdefghijklmnopqrstuvwxyz"
    dn = len(d)
    if N < dn:
        return d[:N]
    freq = math.ceil(N/dn)
    n2 = int(N/freq)
    return "".join([d[:n2]]*freq)


if __name__ == "__main__":
    N = 5
    print(f"solution of {N} is= {solution(N)}")
    N = 1
    print(f"solution of {N} is= {solution(N)}")
    N = 3
    print(f"solution of {N} is= {solution(N)}")
    N = 30
    print(f"solution of {N} is= {solution(N)}")

    N = 26
    print(f"solution of {N} is= {solution(N)}")
    N = 26*2
    print(f"solution of {N} is= {solution(N)}")
    N = 60
    print(f"solution of {N} is= {solution(N)}")