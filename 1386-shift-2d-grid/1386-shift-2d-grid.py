class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)

        l = len(arr)
        n = len(grid[0])
        for i in range(k):
            arr.insert(0, arr[-1])
            arr.pop()
        
        res = []
        for i in range(0, l, n):
            sub_res = []
            for j in range(i, i+n):
                sub_res.append(arr[j])
            res.append(sub_res)
        return res