class Solution:

    # Function to perform case-specific sorting of strings.
    def caseSort(self, s: str, n: int):
        # code here
        s2 = sorted(s)
        lowStart = -1
        ret = [''] * n
        for i, b in enumerate(s2):
            if b.islower():
                lowStart = i
                break
        ld, ud = 0, 0
        for i, b in enumerate(s):
            if b.isupper():
                ret[i] = s2[ud]
                ud += 1
            else:
                ret[i] = s2[lowStart+ld]
                ld += 1
        return ''.join(ret)


sol = Solution()
s = 'defRTSersUXI'
print(f"sort of {s} = {sol.caseSort(s, len(s))}")
s = 'srbDKi'
print(f"sort of {s} = {sol.caseSort(s, len(s))}")

s = 'srbabcdi'
print(f"sort of {s} = {sol.caseSort(s, len(s))}")

s = 'XBZA'
print(f"sort of {s} = {sol.caseSort(s, len(s))}")
