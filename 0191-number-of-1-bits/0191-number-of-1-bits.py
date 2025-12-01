class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n) [2:]
        res = 0
        for i in b:
            if i == "1":
                res += 1
        return res
        