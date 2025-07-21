class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            b = bin(i)[2:]
            if b.count("1") == k:
                res += nums[i]
        return res

        