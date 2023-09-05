from typing import List
from collections import defaultdict


class Solution:
    # def __init__(self) -> None:
    #     self.mapTrie = set()
    #     self.wholeWord = set()
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
