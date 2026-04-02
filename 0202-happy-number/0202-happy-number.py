class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        arr = list(n)
        i = 0
        while i < 100:
            
            res = 0
            for j in arr:
                x = int(j)**2
                res += x
            arr = list(str(res))
            if res == 1:
                return True
            i+=1
        return False
        