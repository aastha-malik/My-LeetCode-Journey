class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 2:
            return [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        j = 0

        while j < numRows-2:
            nums = [1]
            
            for i in range(len(res[-1]) -1):
                nums.append(res[-1][i] + res[-1][i+1])
            nums.append(1)
            res.append(nums)
            j += 1
        return res




        