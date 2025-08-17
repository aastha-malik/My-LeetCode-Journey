class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = list(set(nums.copy()))
        res = 0
        for i in arr:
            c = nums.count(i)
            if c > res:
                res = c
        for i in arr:
            if res == nums.count(i):
                return i