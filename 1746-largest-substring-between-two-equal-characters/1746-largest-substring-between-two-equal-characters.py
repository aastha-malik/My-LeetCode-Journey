class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l = len(s)
        res = set()
        for i in range(l):
            for j in range(l-1, -1, -1):
                if s[i] == s[j] and i!=j:
                    res.add(j-i-1)
        if len(set(s)) == len(s):
            return -1
        else:
            return max(res)

        
        