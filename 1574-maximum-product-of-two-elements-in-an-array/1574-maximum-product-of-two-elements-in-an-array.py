class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j and (nums[i]-1)*(nums[j]-1) > res:
                    res = (nums[i]-1)*(nums[j]-1)
        return res
        