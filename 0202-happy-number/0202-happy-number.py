class Solution:
    def isHappy(self, n: int) -> bool:
        x = str(n)
        for i in range(10):
            l = len(x)
            s = 0
            for j in range(l):
                a = int(x[j]) ** 2
                s += a
            if s == 1:
                return True
            else:
                x = str(s)
        return False

        