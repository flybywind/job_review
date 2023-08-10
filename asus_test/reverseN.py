def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        if enable_print > 0:
            print(N % 10, end="")
        N = N // 10
    print("", flush=True)

N = 763628
print(f"reverse of {N}", flush=True)
solution(N)

N = 10200
print(f"reverse of {N}")
solution(N)

N = 124000
print(f"reverse of {N}")
solution(N)

N = 10000
print(f"reverse of {N}")
solution(N)

N = 1
print(f"reverse of {N}")
solution(N)