class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s = set()

        if nums.count(nums[0]) == 3:
                return "equilateral"
        res = 0
        if nums[0] + nums[1] > nums[2]:
            res += 1
        if nums[1] + nums[2] > nums[0]:
            res += 1
        if nums[0] + nums[2] > nums[1]:
            res += 1
        
        if res == 3:
            if nums.count(nums[0]) == 2 or nums.count(nums[1]) == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
        
        
            
            
        

        