# https://practice.geeksforgeeks.org/problems/maximum-nesting-depth-of-the-parentheses/1?page=1&difficulty[]=0&difficulty[]=1&category[]=Arrays&category[]=Strings&sortBy=accuracy

class Solution:
    def maxDepth(self, vps: str):
        ps = []
        maxd = 0
        for s in vps:
            if s == '(':
                ps.append(s)
            if s == ')':
                if len(ps) > maxd:
                    maxd = len(ps)
                ps.pop()

        return maxd


class Solution2:
    def findMinSum(self, A, B, N):
        return sum([abs(a-b) for (a, b) in zip(sorted(A), sorted(B))])


if __name__ == "__main__":
    # sol = Solution()
    # Input = "((5+2)(3+4)((6))) "
    # print(f"max depth of {Input} = {sol.maxDepth(Input)}")
    # Input = " (43+4++3)((3)(9))+1 "
    # print(f"max depth of {Input} = {sol.maxDepth(Input)}")
    # Input = "0+9"
    # print(f"max depth of {Input} = {sol.maxDepth(Input)}")
    # Input = "1"
    # print(f"max depth of {Input} = {sol.maxDepth(Input)}")
    sol = Solution2()
    A = [4, 1, 8, 7]
    B = [2, 3, 6, 5]
    print(f"A = {A}, B = {B}, mininum diff sum = {sol.findMinSum(A, B, len(A))}")
    A = [4, 1, 2]
    B = [2, 4, 1]
    print(f"A = {A}, B = {B}, mininum diff sum = {sol.findMinSum(A, B, len(A))}")
