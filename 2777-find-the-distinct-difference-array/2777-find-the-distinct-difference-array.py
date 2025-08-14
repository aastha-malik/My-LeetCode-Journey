class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        diff = []
        for i in range(l):
            prefix = len(set(nums[:i+1]))
            sufix = len(set(nums[i+1:]))
            diff.append(prefix - sufix)
        
        return diff
        