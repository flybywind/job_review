'''
Description of the problem:
Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces out of N pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must be greater than or equal to a given threshold X.

Woolly is interested in the number of different ways in which he can build a pen. Pens are considered different if the sets of lengths of their sides are different. For example, a pen of size 1×4 is different from a pen of size 2×2 (although both have an area of 4), but pens of sizes 1×2 and 2×1 are considered the same.

Write a function:

def solution(A, X)

that, given an array A of N integers (containing the lengths of the available pieces of fence) and an integer X, returns the number of different ways of building a rectangular pen satisfying the above conditions. The function should return −1 if the result exceeds 1,000,000,000.

For example, given X = 5 and the following array A:

  A[0] = 1
  A[1] = 2
  A[2] = 5
  A[3] = 1
  A[4] = 1
  A[5] = 2
  A[6] = 3
  A[7] = 5
  A[8] = 1


the function should return 2. The figure above shows available pieces of fence (on the left) and possible to build pens (on the right). The pens are of sizes 1x5 and 2x5. Pens of sizes 1×1 and 1×2 can be built, but are too small in area. It is not possible to build pens of sizes 2×3 or 3×5, as there is only one piece of fence of length 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
X is an integer within the range [1..1,000,000,000];
each element of array A is an integer within the range [1..1,000,000,000].

'''
from collections import defaultdict
from bisect import bisect_left
from math import sqrt, ceil
def solution(A, X):
    # Implement your solution here
    largestBorder = int(sqrt(X))
    counter = defaultdict(int)
    possibleFence = []
    for i, f in enumerate(A):
        counter[f] += 1
        if counter[f] == 2:
            possibleFence.append(f)
            # 应该分成2个counter，不要试图在一个里面都处理了！
        if counter[f] == 4:
            possibleFence.append(f+0.5)
    
    possibleFence = sorted(possibleFence)
    fenCnt = len(possibleFence)
    # largestBorder = min(largestBorder, int(sqrt(possibleFence[-1])))
    rightPos = min(fenCnt, bisect_left(possibleFence, largestBorder)+1)
    if rightPos < fenCnt and (not isinstance(possibleFence[rightPos], int)):
        rightPos += 1

    solCnt = 0
    print(f"possible fen: {possibleFence}")
    for i in range(0, rightPos):
        f = possibleFence[i]
        if not isinstance(f, int):
            continue
        j = ceil(X/f)
        l = bisect_left(possibleFence, j)
        if l >= fenCnt:
            continue
        if possibleFence[l] == f:
            l+=1
        rightCnt = fenCnt - l
        solCnt += rightCnt
        print(f"{f} x (>={j}): {rightCnt}")
        if solCnt > 1_000_000_000:
            return -1
    if rightPos < fenCnt:
        solCnt += int((fenCnt-rightPos) / 2 * (fenCnt-rightPos-1))
    if solCnt > 1_000_000_000:
        return -1
    return solCnt

if __name__ == '__main__':
    # A = [1,2,5,1,1,2,3,5,1]
    # X = 5
    # print(f"solution number for {A} given size <= {X} is {solution(A, X)}") # 2
    
    # A = [1,2,5,1,1,2,3, 3, 5,1]
    # X = 5
    # print(f"solution number for {A} given size <= {X} is {solution(A, X)}") # 4

    # A = [1, 2, 5, 1, 1, 2, 3, 3, 5,1]
    # X = 3
    # print(f"solution number for {A} given size <= {X} is {solution(A, X)}") # 5

    # A = [1, 2, 5, 1, 1, 2, 3, 3, 5, 1]
    # X = 1
    # print(f"solution number for {A} given size <= {X} is {solution(A, X)}")

    # A = [1, 2, 5, 1, 1, 2, 3, 3, 5, 1]
    # X = 100
    # print(f"solution number for {A} given size <= {X} is {solution(A, X)}")

    A = [1, 2, 5, 1, 1, 2, 3, 3, 5, 5, 5, 5, 1, 10, 10, 4, 20, 4, 6, 7, 9, 8, 6, 6, 7, 7, 11, 11, 13]
    X = 20
    print(f"solution number for {A} given size <= {X} is {solution(A, X)}")