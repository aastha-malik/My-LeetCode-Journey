class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n+1):
            arr.append(str(i))
        res = sorted(arr)
        for i in range(n):
            res[i] = int(res[i])
        return res