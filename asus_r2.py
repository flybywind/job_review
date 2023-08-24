"""
'A' -> "1"
'B' -> "2"
…
'J' -> “10”
'K' -> “11”
'Z' -> "26"
 
Example:
# 1      ->    1 (A)        
# 12    ->    2 (AB,     L)
# 123  ->    3 (ABC , LC, AW )  
 
input: 0-9 string
output: a number

"""
class Solution:
    def __init__(self) -> None:
        # self.charmap = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
        pass 

    def parseNum(self, inp:str) -> int:
        # s[i] = if s[:i] is a valid char ?
        #         yes: 1 + s[i:] (i = 1...n)
        #         no:   (return) 
        n = len(inp)
        if n <= 1:
            if inp == '0':
                return 0
            return 1
        pos_num = 0
        findInvaid = False
        for i in range(1, n+1):
            ind = int(inp[:i])
            if ind > 0 and ind <= 26:
                r = self.parseNum(inp[i:])
                if r >= 0:
                    pos_num += r
            else:
                findInvaid = True
                break 

        if findInvaid and pos_num == 0:
            return 0
        
        return pos_num
    

sol = Solution()
inp = "123"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 3}")

inp = "012"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 0}")

inp = "901"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 0}")

inp = "1030"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 0}")

# 100221 > 0
inp = "100221"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 0}")

# 102213 > 5
inp = "102213"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 5}")

# 102213123 > 15
inp = "102213123"
print(f"{inp} has {sol.parseNum(inp)} variances, test pass ?{sol.parseNum(inp) == 15}")
