class Solution:
    def removedup(self, S):
        ret = []
        i = 1
        while i < len(S):
            while S[i-1] == S[i] and i < len(S):
                i += 1
            ret.append(S[i])
        if len(ret) == len(S):
            return S 
        else:
            return self.removedup(S)
        
    def rremove (self, S):
        if len(S) < 4:

        mid = len(S)//2
        if 

    # def rremove (self, S):
	# 	#code here
    #     lastpos = [0]*len(S)
    #     for i in range(1, len(S)):
    #         if S[i] == S[i-1]:
    #             lastpos[i] = lastpos[i-1]
    #         else:
    #             if lastpos[i-1] != i-1:
    #                 parent = lastpos[i-1]
    #                 while parent != 0:
    #                     p2 = lastpos[parent-1]
    #                     if lastpos[parent-1] != parent-1:
    #                         parent = p2
    #                     else:
    #                         break
    #                 # start of the continuous region
    #                 if parent == 0:
    #                     lastpos[i] = i
    #                 else:
    #                     if S[parent-1] == S[i]:
    #                         if lastpos[parent-1] == parent-1:
    #                             lastpos[i] = lastpos[parent-1]
    #                         else:
    #                             lastpos[i] = i
    #                     else:
    #                         lastpos[i] = i
    #             else:
    #                 lastpos[i] = i
    #     for i in range(len(S)-1, -1, -1):
    #         if lastpos[i] != i and lastpos[i] >= 0:
    #             lastpos[lastpos[i]] = -1
    #             lastpos[i] = -1
    #     return ''.join(b for i,b in enumerate(S) if lastpos[i] >= 0)
    
if __name__ == '__main__': 
    ob = Solution()
    S = "abccbccba"
    print("output:", ob.rremove(S))
    S = "abccbaccba" # abbaba --> aaba --> ba
    print(f"output of {S}: {ob.rremove(S)}")
    S = "geeksforgeek" # 
    print(f"output of {S}: {ob.rremove(S)}")
    S = "acaaabbbacdddd" # acac
    print(f"output of {S}: {ob.rremove(S)}")