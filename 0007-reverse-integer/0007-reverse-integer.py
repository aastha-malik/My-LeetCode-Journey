class Solution:
    def reverse(self, x: int) -> int:
        
        s = list(str(abs(x)))
        l = len(s) 
        for i in range(l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        res = int("".join(s))
        if res > 2**31 - 1 or res < -2**31:
            return 0
        if x > 0:
            return res
        else:
            a = "-" + str(res)
            return int(a)