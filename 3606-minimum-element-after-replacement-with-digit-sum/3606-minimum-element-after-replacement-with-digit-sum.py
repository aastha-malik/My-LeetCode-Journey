class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = list(str(nums[i]))
            for j in range(len(nums[i])):
                nums[i][j] = int(nums[i][j])
            nums[i] = sum(nums[i])

        return min(nums)
        

        