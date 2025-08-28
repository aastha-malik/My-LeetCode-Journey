class Solution:
    def countDigits(self, num: int) -> int:
        s = list(str(num))
        res = 0
        for i in range(len(s)):
            if num % int(s[i]) == 0:
                res += 1
        return res

        