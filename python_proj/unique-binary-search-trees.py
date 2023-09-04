class Solution:
    def __init__(self) -> None:
        self._cache = {}

    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        if n in self._cache:
            return self._cache[n]
        
        m = n-1
        res = 0
        for i in range(m//2+1):
            j = m-i 
            if i != j:
                res += 2*self.numTrees(i)*self.numTrees(j)
            else:
                res += self.numTrees(i)*self.numTrees(j)
        self._cache[n] = res
        return res

sol = Solution()
for i in range(10):
    print(f"types of node = {i} is {sol.numTrees(i)}")


        