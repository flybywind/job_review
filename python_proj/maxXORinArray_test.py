import pytest
import random
from typing import List
from maxXORinArray import Solution


@pytest.fixture
def sol() -> Solution:
    return Solution()


@pytest.fixture()
def randomNums() -> List[List[int]]:
    R = 10
    rnd = random.Random(12345)
    ret = []
    for _ in range(R):
        N = rnd.randint(10, 10000)
        nums = [0]*N
        for i in range(N):
            nums[i] = rnd.randint(1, 1000000)
        ret.append(nums)
    return ret


def xorMaxBR(nums: List[int]) -> int:
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            ans = max(ans, nums[i] ^ nums[j])
    return ans


class TestMaxorInArray:

    def testCase1(self, sol):
        nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
        assert xorMaxBR(nums) == sol.findMaximumXOR(nums)

    def testCase2(self, sol):
        nums = [3, 10, 5, 25, 2, 8]
        assert xorMaxBR(nums) == sol.findMaximumXOR(nums)

    def testCaseRand(self, sol, randomNums):
        all_pass = True
        for nums in randomNums:
            expect = xorMaxBR(nums)
            actual = sol.findMaximumXOR(nums)
            if expect != actual:
                print(f"expect {expect}, got {actual}, arry = {nums}")
                all_pass = False
        assert all_pass
