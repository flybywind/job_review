#!/usr/bin/env python
# -*- encoding: utf8 -*-


def shortest_palindrome(input_str):
    revt = reverse_str(input_str)[:-1]
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
    
def reverse_str(str):
    N = len(str)
    revt = [""]*N
    for i in xrange(N-1, -1, -1):
        revt[N-1-i] = str[i]
    return "".join(revt)


if __name__ == "__main__":
    test_str = [
        ("abcd", "dcbabcd"),
        ("aacecaaa", "aaacecaaa"),
        ("aaabbbbc", "cbbbbaaabbbbc")]
    for i, paire in enumerate(test_str):
        ins = paire[0]
        exp = paire[1]
        output = shortest_palindrome(ins)
        if output != exp:
            print "%2d-th test failed: expect %s, got %s " % (i, exp, output)
        else:
            print "%2d-th tests passed"%(i)