class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i = 0
        j = l-1
        res = 0
        while i < j:
            h = min(height[i], height[j])
            water = (j - i) * h
            res = max(water, res)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res
            
        