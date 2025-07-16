class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = 0
        for i in nums:
            if i % 3 != 0:
                arr += 1
        
        
        return arr                
