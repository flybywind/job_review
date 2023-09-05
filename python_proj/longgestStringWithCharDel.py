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
        itered = set()

        def _recurs(s, strN, pre, i):
            nonlocal ans
            if i >= strN:
                return
            if pre in itered:
                return
            itered.add(pre)
            for j in range(i, strN):
                potentialLen = (strN - j) + len(pre)
                if potentialLen < len(ans):
                    return

                pre2 = pre + s[j]
                # print(f"ans = {ans}, iter {pre2} at {j}")

                if pre2 in mapTrie:
                    # print(f"search {pre2} from {j+1}")
                    if pre2 in wholeWord:
                        if len(pre2) > len(ans):
                            ans = pre2
                        elif len(pre2) == len(ans) and pre2 < ans:
                            ans = pre2
                    _recurs(s, strN, pre2, j+1)

        _recurs(s, len(s), '', 0)
        return ans
