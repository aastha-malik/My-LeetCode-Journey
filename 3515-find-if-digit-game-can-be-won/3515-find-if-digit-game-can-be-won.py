class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i+1] > 9:
                s1 = sum(nums[:i+1])
                s2 = sum(nums[i+1:])
                return s1 != s2
        
        if nums[-1] < 10:
            return True
        elif nums[0] >9:
            return True