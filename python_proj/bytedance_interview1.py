def findMaxUniqSubstr(s: str) -> int:
    left = 0
    curdict = {s[left]: 0}
    maxlen = 1
    for right in range(1, len(s)):
        if s[right] in curdict:
            left = curdict[s[right]]+1
        else:
            curdict[s[right]] = right
            n = right - left + 1
            if n > maxlen:
                maxlen = n

    return maxlen


s = "ababcabcdeabc"
print(findMaxUniqSubstr(s))
