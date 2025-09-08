class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        else:
            d = dict(zip(s, t))
            res = 0
            for i in range(len(s)):
                if d[s[i]] == t[i]:
                    res += 1
            return res == len(s)