class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(nums)
        x = len(nums)
        res =( x*(x+1))//2
        
        return res - n