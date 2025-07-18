class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            total = mat[i][i] + mat[i][len(mat) - 1 - i]
            
            sum+=total

        if len(mat) % 2 != 0:
            l = int( (len(mat) - 1) / 2 )
            sum -= mat[l][l]
        return sum