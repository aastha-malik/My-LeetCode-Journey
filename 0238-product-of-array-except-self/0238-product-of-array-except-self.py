class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        res = 1

        if 0 not in nums:
            for i in nums:
                res *= i
            
            for i in nums:
                arr.append(res // i)
            return arr
        if nums.count(0) > 1:
            for i in range(len(nums)):
                arr.append(0)
            return arr
        else:
            for i in nums:
                if i != 0:
                    res *= i
            
            for i in nums:
                if i != 0:
                    arr.append(0)
                else:
                    arr.append(res)
            return arr

            