class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        s = set()
        for x in range(l):
            for y in range(l):
                s.add((y,x,matrix[x][y]))
        
        for i in s:
            matrix[i[0]][i[1]] = i[2]

        for i in range(l):
            for j in range(l//2):
                matrix[i][j], matrix[i][l-j-1] = matrix[i][l-j-1], matrix[i][j]




