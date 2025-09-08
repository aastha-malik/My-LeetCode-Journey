class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        if len(set(s)) != len(set(t)):
            return False
        else:
            for i in range(len(s)):
                d[s[i]] = t[i]
            res = 0
            for i in range(len(s)):
                if d[s[i]] == t[i]:
                    res += 1
            return res == len(s)