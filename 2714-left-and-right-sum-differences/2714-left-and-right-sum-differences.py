class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)

        leftsum = [0]
        for i in range(1,l):
            total = sum(nums[:i])
            leftsum.append(total)
        
        rightsum = [0]
        for i in range(l-2, -1, -1):
            total = sum(nums[i+1:])
            rightsum.insert(0, total)
        
        res = []
        for i in range(l):
            total = abs(leftsum[i] - rightsum[i])
            res.append(total)
        return res

        