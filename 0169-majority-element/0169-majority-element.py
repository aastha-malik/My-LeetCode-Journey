class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        l = len(nums)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                x = d[i]
                x += 1
                d[i] = x
        
        for i, j in d.items():
            if j > l//2:
                return i
