class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0

        n = len(height)

        i = 0
        j = n - 1
        while i < j:
            l = j - i
            r = min(height[i], height[j])
            if l * r > m:
                m = l * r
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m



        