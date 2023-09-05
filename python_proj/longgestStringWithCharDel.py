from typing import List
from collections import defaultdict
import heapq


class HeapNode:
    def __init__(self, prefix, p) -> None:
        self.prefix = prefix
        self.potential = 0
        self.currentPos = p

    def __lt__(self, other) -> bool:
        return self.potential > other.potential

    def __repr__(self) -> str:
        return f"{self.prefix}@{self.currentPos}, potential = {self.potential}"


class Solution:
    # def __init__(self) -> None:
    #     self.mapTrie = set()
    #     self.wholeWord = set()
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        mapTrie = defaultdict(int)  # prefix and its potential longgest word
        wholeWord = set(dictionary)
        for word in dictionary:
            wn = len(word)
            for i in range(1, len(word)+1):
                if mapTrie[word[:i]] < wn:
                    mapTrie[word[:i]] = wn
        strN = len(s)
        occurPos = [strN]*26
        for p, b in enumerate(s):
            i = ord(b) - ord('a')
            if occurPos[i] > p:
                occurPos[i] = p

        heapAry = []
        for i, p in enumerate(occurPos):
            hn = HeapNode('', p)
            hn.potential = strN - p
            if hn.potential > 0:
                heapAry.append(hn)

        heapq.heapify(heapAry)
        ans = ''
        visited = set()
        while len(heapAry) > 0:
            hn: HeapNode = heapq.heappop(heapAry)
            # print(f"<<| pop heap: {hn}")
            for i in range(hn.currentPos, strN):
                prefix2 = hn.prefix + s[i]
                if prefix2 in visited:
                    # print(f"skip, {prefix2} has visited")
                    continue
                visited.add(prefix2)
                if prefix2 in wholeWord:
                    if len(prefix2) > len(ans) or \
                            (len(prefix2) == len(ans) and prefix2 < ans):
                        ans = prefix2
                        # print(f"find ans: {ans}")
                        heapAry = [
                            hn for hn in heapAry if hn.potential >= len(ans)]
                        heapq.heapify(heapAry)

                hn2 = HeapNode(prefix=prefix2, p=i+1)
                hn2.potential = min(
                    strN - i - 1 + len(hn2.prefix), mapTrie[hn2.prefix])
                if hn2.potential >= len(ans):
                    # print(f">> push heap: {hn2}")
                    heapq.heappush(heapAry, hn2)

        return ans
