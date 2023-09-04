import math
from typing import List


class Solution:

    def supperpalindromes10000(self, lower, upper) -> List[int]:
        ret = 0
        lower_s = int(math.sqrt(lower))
        upper_s = int(math.sqrt(upper)) + 1
        for i in range(lower_s, upper_s):
            i2 = i**2
            if i2 <= upper and i2 >= lower and self._check(i) and self._check(i2):
                ret += 1
        return ret

    def _check(self, n: int) -> bool:
        if n < 10:
            return True
        s = str(n)
        l = len(s)
        return s[:l//2] == s[-1:l//2-1:-1] if l % 2 == 0 else s[:l//2] == s[-1:l//2:-1]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        lower, upper = int(left), int(right)
        if upper < 10000:
            return self.supperpalindromes10000(lower, upper)

        left = int(math.sqrt(int(left)))
        right = int(math.sqrt(int(right)))
        ret = 0

        def _halfen(s: int) -> int:
            if s < 9:
                return int(s)
            n = len(str(s))//2
            return int(s//(10**n))

        def _padding(s: int) -> (int, int):
            s1 = s
            s0 = s
            nums = []
            while s0 > 0:
                nums.append(s0 % 10)
                s0 = s0//10
            for i in nums[1:]:
                s1 = s1*10 + i

            s2 = s
            for i in nums:
                s2 = s2*10 + i
            return (s1, s2)

        right = _halfen(right*3)
        left = _halfen(left/10)
        for i in range(left, right+1):
            s1, s2 = _padding(i)
            s1, s2 = s1**2, s2**2
            if s1 <= upper and s1 >= lower and self._check(s1):
                ret += 1
            if s2 <= upper and s2 >= lower and self._check(s2):
                ret += 1
        return ret
