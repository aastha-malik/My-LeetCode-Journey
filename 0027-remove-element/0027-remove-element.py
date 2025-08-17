class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                #nums.append("_")
            else:
                res += 1
                i+= 1
        return res
        return nums 
        