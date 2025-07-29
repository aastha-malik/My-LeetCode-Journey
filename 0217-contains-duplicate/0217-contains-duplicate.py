class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        nums.sort()
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        