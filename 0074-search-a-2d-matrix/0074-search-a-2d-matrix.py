class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        n = len(matrix[0])
        l = 0
        while low <= high:
            mid = (low+high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                h = len(matrix[mid]) - 1
                while l <= h:
                    m = (l+h)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        h = m - 1
                return l < len(matrix[low]) and matrix[low][l] == target
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                high = mid - 1
        # l = 0
        # h = len(matrix[low]) - 1
        # while l <= h:
        #     m = (l+h)//2
        #     if matrix[low][m] == target:
        #         return True
        #     elif matrix[low][m] < target:
        #         l = m + 1
        #     else:
        #         h = m - 1
        return False
        