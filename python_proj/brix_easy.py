class Solution:
    def qn2(self, str):
        stk = []
        for s in str:
            if s == '(':
                stk.append(s)
            elif s == ')':
                if len(stk) > 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    return False

        return len(stk) == 0


sol = Solution()
str = "()"
print(f"{str} valid: {sol.qn2(str)}")

str = "()()"
print(f"{str} valid: {sol.qn2(str)}")

str = "(()())"
print(f"{str} valid: {sol.qn2(str)}")

str = "((1)(3+45))"
print(f"{str} valid: {sol.qn2(str)}")

str = "((1)(3+45)))"
print(f"{str} valid: {sol.qn2(str)}")

str = "((1)((3+45)))"
print(f"{str} valid: {sol.qn2(str)}")
