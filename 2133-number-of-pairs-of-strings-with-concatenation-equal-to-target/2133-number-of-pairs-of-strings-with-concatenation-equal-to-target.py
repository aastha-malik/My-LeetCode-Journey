class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if nums[i] + nums[j] == target and i!=j:
                    res += 1
        return res
        