class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        diff = s % k
        return diff

        