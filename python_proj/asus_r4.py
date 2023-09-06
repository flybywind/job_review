# input array:
# [[start, end],
#  [start, end]]
# [[1,3]
#   [2, 4]] . => [[1,4]]
from typing import List


def mergeRange(ranges: List[List[int]]) -> List[List[int]]:
    if len(ranges) <= 1:
        return ranges

    ranges_sort = sorted(ranges, key=lambda a: a[0])

    ret = [[]]
    for rng in ranges_sort:
        last = ret[-1]
        if len(last) == 0:
            ret[-1] += rng
        else:
            if last[1] >= rng[0]:
                ret[-1] = [min(last[0], rng[0]), max(last[1], rng[1])]
            else:
                ret.append(rng)

    return ret


# integer array : [-10, 1,2,3,4,5,6,9,8,7] size < 20
# select some num:
# 4,5,6 ==> 4*1 + 5*2 + 6*3 == 32

# [-2, -1, 1, 2, 3]  N = 5
# m = 3 only positive ==> 1,2,3 ==> f(3) = 14
# m = 4 [-1,1,2,3]  => f(4) = f(3) + sum([1,2,3]) = 20
# m = 5 untile f reduce


def findMaxByformula(ary):
    ary_sort = sorted(ary)
    # find positive pos
    pp = 0
    for i, n in enumerate(ary_sort):
        if n >= 0:
            pp = i
            break

    m = len(ary) - pp
    ss = sum(ary_sort[pp:])
    fm = sum([e*(i+1) for i, e in enumerate(ary_sort[pp:])])
    print(f"find first large num at: {pp}, m = {m}, {fm}")
    while pp > 0:
        m += 1
        pp -= 1
        fm2 = fm + ss + ary_sort[pp]
        if fm2 > fm:
            print(f"find larger num at: {pp}, m = {m}, {fm2}")
            fm = fm2
        else:
            break
    return fm
