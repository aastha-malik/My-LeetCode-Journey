class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        l = len(nums)
        for i in range(0, l, 2):
            res += nums[i]
        return res
        