class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        for i in range(len(nums)):
            if nums[i] == "6":
                nums = nums[:i] + "9" + nums[i+1:]
                return int(nums)
        return int(nums)
        
        