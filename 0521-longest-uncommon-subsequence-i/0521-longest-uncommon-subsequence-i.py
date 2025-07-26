class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        l = len(a)
        s1 = 0
        for i in range(l):
            for j in range(l, i-1, -1):
                if a[i:j] not in  b:
                    if s1 < len(a[i:j]):
                        s1 = len(a[i:j])

        
        n = len(b)
        s2 = 0
        for i in range(n):
            for j in range(n, i-1, -1):
                if b[i:j] not in  a:
                    if s2 < len(b[i:j]):
                        s2 = len(b[i:j])

        if a != b:
            return max(s1, s2)
        else:
            return -1
        