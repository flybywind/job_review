def max_sum(a, n):
    # counter-clock wise
    # 1,2,3,4, ==> 2,3,4, 1 ==> 3, 4, 1, 2 ==> 4, 1, 2, 3
    sum_cc = 0
    # # 1,2,3,4 => 4, 1, 2, 3 ==> 3, 4, 1, 2 ==> 2, 3, 4, 1 same as counter-clock wise
    # sum_cw = 0
    maxs = 0
    for i in range(0, n):
        if i > 0:
            sum_cc += a[i]
        maxs += i * a[i]
    # move in counter-clock wise:
    a2 = a + a
    cursum = maxs
    for s in range(1, n):
        e = s + n - 1
        cursum -= sum_cc
        cursum += a2[e]*(n-1)
        sum_cc -= a2[s]
        sum_cc += a2[e]
        if cursum > maxs:
            print("1. find max at", s, cursum)
            maxs = cursum

    return maxs


def max_sum_bf(a, n):
    a2 = a + a
    maxs = sum([i*v for i, v in enumerate(a)])
    for i in range(1, n):
        ss = sum([k*a2[i+k] for k in range(n)])
        if ss > maxs:
            print("2. find max at", i, ss)
            maxs = ss
    return maxs


a = [8, 3, 1, 2]
n = len(a)
print(f"max sum of array: {a} is {max_sum(a, n)}, {max_sum_bf(a, n)}")

a = [5, 8, 3, 9, 1, 2, 4]
n = len(a)
print(f"max sum of array: {a} is {max_sum(a, n)}, {max_sum_bf(a, n)}")

a = [9, 5, 8, 3, 9, 4]
n = len(a)
print(f"max sum of array: {a} is {max_sum(a, n)}, {max_sum_bf(a, n)}")

a = [1, 1, 9, 5, 8, 3, 9, 4]
n = len(a)
print(f"max sum of array: {a} is {max_sum(a, n)}, {max_sum_bf(a, n)}")
