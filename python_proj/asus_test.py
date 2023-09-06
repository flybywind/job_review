import pytest
from asus_r4 import mergeRange, findMaxByformula


class TestRangeMerge:
    def testCase1(self):
        ary = [[1, 2], [5, 6], [1, 4], [11, 20], [3, 4], [6, 9], [8, 9]]
        print(mergeRange(ary))

    def testCase2(self):
        ary = [[]]
        print(mergeRange(ary))
        ary = []
        print(mergeRange(ary))

    def testCase3(self):
        ary = [[1, 2], [5, 6], [1, 4], [11, 20], [-1, 4], [6, 9], [8, 9]]
        print(mergeRange(ary))

    def testCase4(self):
        ary = [[1, 2], [5, 6], [1, 4], [11, 20],
               [-1, 4], [6, 9], [8, 9], [-100, 100000]]
        print(mergeRange(ary))
