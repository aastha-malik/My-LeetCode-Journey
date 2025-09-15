class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        res = []
        if target not in nums:
            return [-1, -1]
        else:
            for i in range(l):
                if nums[i] == target:
                    if len(res) <= 1 :
                        res.append(i)
                    else:
                        if i > res[-1]:
                            res[-1] = i
        if len(res) == 1:
            return [res[0], res[0]]
        return res
                    
            