import pytest
from asus_r4 import mergeRange, findMaxByformula


class TestAsus:
    def testCase1(self):
        ary = [1, 2, -1, -2, 3]
        print(findMaxByformula(ary))

    def testCase2(self):
        ary = [-1, 300]
        print(findMaxByformula(ary))

    def testCase3(self):
        ary = [1, 2, -1, -9, 3]
        print(findMaxByformula(ary))
