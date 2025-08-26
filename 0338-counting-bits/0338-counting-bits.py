class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            b = list((bin(i)[2:]))
            s = b.count("1")
            res.append(s)
        return res





        