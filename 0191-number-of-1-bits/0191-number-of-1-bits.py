class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        freq = {
            "0":0,
            "1":0
            }
        for i in n:
            freq[i] += 1
        return freq["1"]