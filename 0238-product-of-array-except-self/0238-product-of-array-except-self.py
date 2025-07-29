class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        if 0 not in nums:
            multiple = 1
            for i in nums:
                multiple *= i
            
            res = []
            for i in nums:
                div = int(multiple / i)
                res.append(div)
            return res
        else:
            multiple = 1
            for i in nums:
                if i != 0:
                    multiple *= i
            
            res = []
            for i in nums:
                if i == 0:
                    div = int(multiple)
                    res.append(div)
                else:
                    res.append(0)
            return res