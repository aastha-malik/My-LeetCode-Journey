class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = max(nums)

        count = [0] * (m + 1)
        for x in nums:
            count[x] += 1
        
        n = 0
        i = 0
        while i < len(count):
            res = 0
            if count[i] > 0:
                while n < len(nums):
                    nums[n] = i
                    res += 1
                    n += 1
                    if res == count[i]:
                        break
            i += 1
        


        
