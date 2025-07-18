class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num = 0
        for i in grid:
            for j in i:
                if j < 0:
                    num += 1
        return num
        