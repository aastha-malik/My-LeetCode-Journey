class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for x in range(l):
            for y in range(x+1,l):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for i in range(l):
            for j in range(l//2):
                matrix[i][j], matrix[i][l-j-1] = matrix[i][l-j-1], matrix[i][j]


