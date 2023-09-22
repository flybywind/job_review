# https://practice.geeksforgeeks.org/problems/optimal-array--170647/1?page=1&difficulty[]=1&category[]=Arrays&category[]=Strings&sortBy=accuracy
from typing import List
from collections import namedtuple

opInfo = namedtuple('opInfo', ['opNum', 'opPos', 'opNeg', 'target'])


class Solution:
    def optimalArray(self, n: int, a: List[int]) -> List[int]:
        # code here
        opPos = opNeg = 0
        avg = a[0]
        # negI: the first index where the element on it is greater than the avg, it indicates the element number that involves neg/pos operations
        # posI, negI = 1, 1
        negI = 1
        sum = a[0]
        opRes = [0]*n

        def _trial(avgNext):
            nonlocal avg, opPos, opNeg, negI
            opPos2 = opPos + (avgNext - avg)*negI
            opNeg2 = opNeg - (avgNext - avg)*(i-negI)
            if opNeg2 < 0:
                opPos2 -= opNeg2
                opNeg2 = 0
            if opPos2 < 0:
                opNeg2 -= opPos2
                opPos2 = 0
            opNeg2 += (a[i] - avgNext)
            if opNeg2 < 0:
                opPos2 -= opNeg2
                opNeg2 = 0
            return opInfo(opPos2 + opNeg2, opPos2, opNeg2, avgNext)

        for i in range(1, n):
            avg2 = (sum + a[i])//(1+i)
            opCand = [_trial(avg2), _trial(avg2-1), _trial(avg2+1)]
            d = 1
            flag = 1
            bestOp = opCand[0]
            keepTrial = False
            if opCand[1].opNum < opCand[0].opNum:
                bestOp = opCand[1]
                flag = -1
                keepTrial = True
            elif opCand[2].opNum < opCand[0].opNum:
                bestOp = opCand[2]
                keepTrial = True

            while keepTrial:
                d += 1
                opNext = _trial(avg2 + flag*d)
                if opNext.opNum < bestOp.opNum:
                    bestOp = opNext
                else:
                    keepTrial = False

            opRes[i], opPos, opNeg, avg = bestOp
            # while a[posI] < avg:
            #     posI += 1
            # negI = posI
            while a[negI] <= avg:
                negI += 1
            sum += a[i]
        return opRes


sol = Solution()
# arr = [1, 6, 9, 12]
# n = len(arr)
# print(f"optimal operation num for array {arr} is {sol.optimalArray(n, arr)}")

arr = [1, 1, 1, 7, 7, 10, 19]
n = len(arr)
print(f"optimal operation num for array {arr} is {sol.optimalArray(n, arr)}")
