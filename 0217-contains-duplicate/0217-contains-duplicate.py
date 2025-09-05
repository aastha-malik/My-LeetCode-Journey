class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        return len(d) != len(nums)
