class Solution:
    def mySqrt(self, x: int) -> int:
        root = str(x ** (0.5))
        for i in range(len(root)):
            if root[i] == ".":
                return int(root[:i])
        return int(root)
        