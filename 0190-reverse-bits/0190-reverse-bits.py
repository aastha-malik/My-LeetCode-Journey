class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n & 0xffffffff, '032b')
        n = str(n)
        l = len(n)
        for i in range(l//2):
            n = list(n)
            n[i], n[l - i - 1] = n[l - i - 1], n[i]
            n = "".join(n)
        return int(n, 2)