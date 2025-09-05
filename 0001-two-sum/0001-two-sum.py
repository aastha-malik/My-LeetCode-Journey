class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        d = {}

        for i in range(l):
            d[nums[i]] = i

        for i in range(l):
            n = target - nums[i]
            if n in d and d[n] != i:
                return [i, d[n]]