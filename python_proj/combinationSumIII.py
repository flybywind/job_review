class Solution:
    def combinationSum(self, K, target):
        def _recur(K, start, target):
            ret = []
            for i in range(start, 10):
                target1 = target - i
                if target1 < 0:
                    return ret
                if target1 == 0 and K == 1:
                    return [[i]]
                else:
                    if K > 1:
                        ret2 = _recur(K-1, i+1, target1)
                        if len(ret2) > 0:
                            ret += [[i]+r for r in ret2]
            return ret
        return _recur(K, 1, target)


sol = Solution()
K = 3
target = 7
print(f"K = {K}, N = {target}, combination = {sol.combinationSum(K, target)}")

K = 3
target = 9
print(f"K = {K}, N = {target}, combination = {sol.combinationSum(K, target)}")

K = 4
target = 3
print(f"K = {K}, N = {target}, combination = {sol.combinationSum(K, target)}")


K = 3
target = 20
print(f"K = {K}, N = {target}, combination = {sol.combinationSum(K, target)}")

K = 4
target = 20
print(f"K = {K}, N = {target}, combination = {sol.combinationSum(K, target)}")
