class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        arr = set(nums)
        return len(arr) != len(nums)