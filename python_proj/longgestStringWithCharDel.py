from typing import List
from collections import defaultdict

# https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/solutions/996014/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/ 双指针

"""
# 尝试了静态数组代替defaultdict，发现并不能减少内存使用

from typing import List
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.queryPos = []
        self.dictPos = [0]*26
        self.queryPosCnt = [0]*26
        for _ in range(26):
            self.queryPos.append([0]*10)

    def cleanQueryPos(self):
        self.queryPosCnt = [0]*26

    def appendQueryPos(self, idx, p):
        if len(self.queryPos[idx]) == self.queryPosCnt[idx]:
            self.queryPos[idx] += [0]*(1+self.queryPosCnt[idx])
        self.queryPos[idx][self.queryPosCnt[idx]] = p
        self.queryPosCnt[idx] += 1

    def cleanDictPos(self):
        self.dictPos = [0]*26

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        self.cleanQueryPos()
        for p, b in enumerate(s):
            idx = ord(b) - ord('a')
            self.appendQueryPos(idx, p)

        dictionary = sorted(dictionary, key=lambda s: (-len(s), s))

        for d in dictionary:
            self.cleanDictPos()
            for b in d:
                self.dictPos[ord(b) - ord('a')] += 1

            lenCover = True
            for b in d:
                idx = ord(b)-ord('a')
                cnt = self.dictPos[idx]
                if cnt > self.queryPosCnt[idx]:
                    lenCover = False
                    break
            if not lenCover:
                continue

            lastPos = -1
            found = True
            for b in d:
                idx = ord(b)-ord('a')
                posList = self.queryPos[idx][:self.queryPosCnt[idx]]
                newPos = lastPos
                for p in posList:
                    if p > lastPos:
                        newPos = p
                        break
                if newPos == lastPos:
                    found = False
                    break
                lastPos = newPos
            if found:
                return d
        return ''

"""


class Solution:

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        queryPos = defaultdict(list)
        for p, b in enumerate(s):
            queryPos[b].append(p)
        dictionary = sorted(dictionary, key=lambda s: (-len(s), s))

        for d in dictionary:
            dictPos = defaultdict(int)
            for b in d:
                dictPos[b] += 1

            lenCover = True
            for b, cnt in dictPos.items():
                if cnt > len(queryPos[b]):
                    lenCover = False
                    break
            if not lenCover:
                continue

            lastPos = -1
            found = True
            for b in d:
                posList = queryPos[b]
                newPos = lastPos
                for p in posList:
                    if p > lastPos:
                        newPos = p
                        break
                if newPos == lastPos:
                    found = False
                    break
                lastPos = newPos
            if found:
                return d
