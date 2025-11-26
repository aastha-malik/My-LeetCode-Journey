class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        res = []
        n = nums[0]
        b = int(str(n), 2)
        res.append(b % 5 == 0)
        for i in range(1,len(nums)):
            n = str(n)
            n += str(nums[i])
            
            
            b = int(n, 2)
            res.append(b % 5 == 0)
        
        return res
                

        