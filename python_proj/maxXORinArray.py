from typing import List


def intBitNum(num: int) -> int:
    bit = 0
    while num > 0:
        bit += 1
        num >>= 1
    return bit


class BinTrie:
    def __init__(self, capacity, maxbit):
        self.capacity = int(capacity)
        self.trie = [None]*self.capacity
        self.cnt = 1
        self.maxbit = maxbit
        for i in range(self.capacity):
            self.trie[i] = [0]*2

    def reset(self, maxbit):
        self.cnt = 1
        self.maxbit = maxbit
        for i in range(self.capacity):
            self.trie[i][0] = self.trie[i][1] = 0

    def insert(self, num):
        cur = 0
        for i in range(self.maxbit-1, -1, -1):
            bit = (num >> i) & 1
            nextnode = None if cur >= len(self.trie) else self.trie[cur]
            if nextnode is None:
                self.capacity += self.cnt
                for _ in range(self.cnt):
                    self.trie.append([0]*2)
                nextnode = self.trie[cur]

            if nextnode[bit] == 0:
                nextnode[bit] = self.cnt
                self.cnt += 1
            cur = nextnode[bit]

    def lookup(self, num: int) -> int:
        cur = 0
        ans = 0
        for i in range(self.maxbit-1, -1, -1):
            bit = ((num >> i) & 1) ^ 1
            nextnode = self.trie[cur]
            if nextnode[bit] == 0:
                bit = bit ^ 1
            ans = (bit << i) + ans
            cur = nextnode[bit]
        return ans


class Solution:
    # def __init__(self, cap=100) -> None:
    #     self.trie = BinTrie(cap)

    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxbit = intBitNum(max(nums))
        trie = BinTrie(100, maxbit)
        for n in nums:
            trie.insert(n)

        ans = 0
        for n in nums:
            ans = max(ans, n ^ trie.lookup(n))
        return ans
