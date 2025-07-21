class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = max(nums)
        for i in range(k-1):
            res += (max(nums) + i + 1)
        return res
        
        