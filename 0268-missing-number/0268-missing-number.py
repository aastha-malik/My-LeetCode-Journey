class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == nums[-1] + 1:
            return max(nums) + 1
        else:
            for i in range(len(nums)):
                if i != nums[i]:
                    return i

            
        