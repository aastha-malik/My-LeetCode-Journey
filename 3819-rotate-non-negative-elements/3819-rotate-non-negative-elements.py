class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        idx = [i for i, x in enumerate(nums) if x>= 0]
        vals = [nums[i]for i in idx]
        
        
        if not vals:
            return nums

        k %= len(vals)
        rotated = vals[k:] + vals[:k]
        for i, v in zip(idx, rotated):
            nums[i] = v
        return nums