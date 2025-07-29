class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        arr = list(set(nums))
        return len(arr) != l