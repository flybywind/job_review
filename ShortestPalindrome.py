#!/usr/bin/env python
# -*- encoding: utf8 -*-


class Solution(object):
    def shortestPalindrome(self, input_str):
        """
        :type s: str
        :rtype: str
        """
        if input_str is None:
            return None
        if len(input_str) == 0:
            return ""
        revt = self.reverse_str(input_str)[:-1]
        N = len(input_str)
        j = k = 0
        while j < N-1:
            for i in xrange(N):
                while j < N - 1 and revt[j] == input_str[j-k]:
                    j+=1
                if j >= N-1: break
                j = k = i + 1
        if j == N-1:
            if k > 0:
                return revt[:k] + input_str
            else: 
                return input_str
        
    def reverse_str(self, str):
        return str[::-1]



if __name__ == "__main__":
    test_str = [
        ("aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa"),
        ("abcd", "dcbabcd"),
        ("aacecaaa", "aaacecaaa"),
        ("aaabbbbc", "cbbbbaaabbbbc")        ]
    s = Solution()
    for i, paire in enumerate(test_str):
        ins = paire[0]
        exp = paire[1]
        output = s.shortestPalindrome(ins)
        if output != exp:
            print "%2d-th test failed: expect %s, got %s " % (i, exp, output)
        else:
            print "%2d-th tests passed"%(i)