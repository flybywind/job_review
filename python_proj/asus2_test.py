import pytest
from asus_r5 import findDup


class TestAsus:
    def testCase1(self):
        # N = 6
        ary = [1, 2, 3, 3, 3, 4]
        print(findDup(ary))

    def testCase2(self):
        # N = 6
        ary = [2, 1, 3, 4, 5, 2]
        print(findDup(ary))

    def testCase3(self):
        # N = 6
        ary = [1, 2, 2, 2, 2, 2]
        print(findDup(ary))
