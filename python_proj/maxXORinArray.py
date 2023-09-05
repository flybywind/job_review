from typing import List


def intBitNum(num: int) -> int:
    bit = 0
    while num > 0:
        bit += 1
        num >>= 1
    return bit


class BinTrie:
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.trie = []
        self.cnt = 1
        self.maxbit = 31
        for _ in range(self.capacity):
            self.trie.append([0]*2)

    def reset(self, maxbit):
        self.cnt = 1
        self.maxbit = maxbit
        for i in range(self.capacity):
            self.trie[i][0] = self.trie[i][1] = 0

    def insert(self, num):
        mask = 1 << (self.maxbit-1)
        cur = 0
        while mask > 0:
            bit = 1 if num & mask else 0
            mask = mask >> 1
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
        mask = 1 << (self.maxbit-1)
        cur = 0
        ans = 0
        while mask > 0:
            bit = 1 if (num & mask) ^ mask else 0
            mask = mask >> 1
            nextnode = self.trie[cur]
            if nextnode[bit] == 0:
                bit = bit ^ 1
            ans = (ans << 1) + bit
            cur = nextnode[bit]
        return ans


class Solution:
    def __init__(self, cap=100) -> None:
        self.trie = BinTrie(cap)

    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxbit = intBitNum(max(nums))
        self.trie.reset(maxbit)
        for n in nums:
            self.trie.insert(n)

        ans = 0
        for n in nums:
            ans = max(ans, n ^ self.trie.lookup(n))
        return ans
