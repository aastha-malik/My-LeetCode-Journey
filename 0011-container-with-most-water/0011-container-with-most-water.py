class Solution:
    def maxArea(self, height: List[int]) -> int:
        #b => base   and h => heigth (lesser one)
        i = 0
        j = len(height) - 1
        max_amount = 0
        while i < j:
            b = j-i
            h = min(height[i], height[j])
            amount = b * h
            if amount > max_amount:
                max_amount = amount
            if  height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_amount
