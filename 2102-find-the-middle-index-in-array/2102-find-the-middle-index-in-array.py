class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        if len(nums) <= 1:
            return 0
        for i in range(1,len(nums)):
            sum1 = sum(nums[:i])
            sum2 = sum(nums[i+1:])
            if sum1 == sum2:
                return i
        return -1