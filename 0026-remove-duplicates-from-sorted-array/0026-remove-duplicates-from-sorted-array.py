class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        i = 1
        while i < len(nums):

            if nums[i] == nums[i-1]:
                nums.pop(i)
                n += 1
            else:
                i+=1
        return len(set(nums))

        