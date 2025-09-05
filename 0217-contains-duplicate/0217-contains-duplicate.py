class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set(nums)
        return len(d) != len(nums)
