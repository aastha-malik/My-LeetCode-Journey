class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and nums[j] - nums[i] > res:
                    res = nums[j] - nums[i]
        if res == 0:
            return -1
        return res
        