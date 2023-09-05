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

        def _recurs(s, strN, pre, i):
            nonlocal ans
            if i == strN:
                return
            for j in range(i, strN):
                potentialLen = (strN - j) + len(pre)
                if potentialLen < len(ans):
                    break
                pre2 = pre + s[j]
                if pre2 in mapTrie:
                    if pre2 in wholeWord:
                        if len(pre2) > len(ans):
                            ans = pre2
                        elif len(pre2) == len(ans) and pre2 < ans:
                            ans = pre2
                    _recurs(s, strN, pre2, j+1)

            return

        _recurs(s, len(s), '', 0)
        return ans
