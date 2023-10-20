# 1234 ==> 4231
# 10 => 1 ?
# 41 =>
# 192 => 912
# 1294 =>
# 919 => 991
# 9817 ==> 9871


def swap2bitMax(num):
    num_ary_map = [-1]*10
    num_ary = [''] * len(num)
    i = 0
    for i, s in enumerate(num):
        num_ary_map[ord(s)-ord('0')] = i
        num_ary[i] = s

    for i, s in enumerate(num):
        o = ord(s) - ord('0')
        for n in range(9, o, -1):
            if num_ary_map[n] > i:
                num_ary[i], num_ary[num_ary_map[n]] = str(n), s
                return "".join(num_ary)

    return "".join(num_ary)


nums = "1234"
print(swap2bitMax(nums))
nums = "41"
print(swap2bitMax(nums))
nums = "10"
print(swap2bitMax(nums))
nums = "919"
print(swap2bitMax(nums))
nums = "9817"
print(swap2bitMax(nums))

nums = "98179"
print(swap2bitMax(nums))
