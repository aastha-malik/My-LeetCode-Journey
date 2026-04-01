class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[]
        for i in matrix:
            for j in i:
                res.append(j)
        low = 0
        high = len(res) -1
        while low < high:
            mid = (low + high) //2
            if res[mid] == target:
                return True
            elif res[mid] > target:
                high = mid - 1
            else: 
                low = mid + 1
        return res[low] == target
        