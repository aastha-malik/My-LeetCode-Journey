class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        arr = []
        if m*n != l:
            return []
        for i in range(0, l, n):
            arr.append(original[i:i+n])
        return arr
        