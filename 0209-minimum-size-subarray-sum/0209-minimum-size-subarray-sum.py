class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        total = 0
        ans = len(nums)
        while r < len(nums):
            total +=  nums[r]
            while total >= target:
                ans = min(ans, r-l+1)
                total -= nums[l]
                l += 1
            
            r+=1
        if l == 0:
            return 0
        
        return ans


