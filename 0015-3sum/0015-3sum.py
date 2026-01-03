class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        res = []
        s = set()
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x = 0 - nums[i]
            j = i + 1
            k = l - 1
            while j < k:                    
                if nums[j] + nums[k] == x :
                    res.append([nums[i], nums[j], nums[k] ])
                    while j <k and nums[j] == nums[j + 1]:
                        j += 1
                    while j <k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < x:
                    j += 1
                else:
                    k-=1
                    
                
                    
        return res






