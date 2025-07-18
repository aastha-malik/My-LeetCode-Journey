class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            less = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    less += 1
            arr.append(less)

        return arr
        