from typing import List


class Solution:
    # def __init__(self) -> None:
    #     self.mapTrie = set()
    #     self.wholeWord = set()
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        mapTrie = set()
        wholeWord = set(dictionary)
        for word in dictionary:
            for i in range(1, len(word)+1):
                mapTrie.add(word[:i])

        ans = ""
        pruneCache = set()

        def _recurs(s, strN, pre, i):
            nonlocal ans, pruneCache
            if i == strN:
                return
            potentialLen = (strN - i - 1) + len(pre)
            if potentialLen < len(ans):
                return

            key = pre + str(i+1)
            if key not in pruneCache:
                # print(f"search {pre} from {i+1}, skip {i}")
                pruneCache.add(key)
                _recurs(s, strN, pre, i+1)

            pre2 = pre + s[i]
            key = pre2 + str(i+1)
            if key not in pruneCache:
                pruneCache.add(key)
                if pre2 in mapTrie:
                    # print(f"search {pre2} from {i+1}")
                    if pre2 in wholeWord:
                        if len(pre2) > len(ans):
                            ans = pre2
                        elif len(pre2) == len(ans) and pre2 < ans:
                            ans = pre2
                    _recurs(s, strN, pre2, i+1)

        _recurs(s, len(s), '', 0)
        return ans
