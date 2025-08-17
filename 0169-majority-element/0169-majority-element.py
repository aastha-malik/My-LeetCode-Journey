class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        arr = list(set(nums))
        for i in arr:
            if nums.count(i) > (l//2):
                return i