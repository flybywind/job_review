#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        st = 0
        showat = {}
        out = 0
        for i, s in enumerate(S):
            if s in showat:
                st2 = showat[s]
                showat[s] = i
                for j in range(st, st2):
                    if S[j] in showat:
                        del showat[S[j]]
                st = st2+1
                continue
            showat[s] = i
            if out < 1+i-st:
                out = i-st+1
        
        return out

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    S = "geeksforgeeks"
    solObj = Solution()
    ans = solObj.longestSubstrDistinctChars(S)
    print(S, ans)

    S = "abcdefg"
    ans = solObj.longestSubstrDistinctChars(S)
    print(S, ans)
    
    S = "abebcbdefgb"
    ans = solObj.longestSubstrDistinctChars(S)
    print(S, ans)