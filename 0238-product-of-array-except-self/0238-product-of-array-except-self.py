class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        zero = 0
        for i in nums:
            if i != 0:
                ans *= i
            else:
                zero += 1
        
        res = []
        for i in nums:
            if zero == 1:
                if i!= 0:
                    res.append(0)
                else:
                    res.append(ans)
                
            elif zero > 1:
                res.append(0)
            else:
                res.append(ans // i)

        return res
        