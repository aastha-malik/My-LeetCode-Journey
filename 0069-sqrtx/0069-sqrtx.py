class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid**2 == x:
                return mid
            elif mid*mid < x:
                s = mid+1
                if s**2 > x:
                    return mid
                else:
                    low = mid+1
            else:
                s = mid-1
                if s**2 < x:
                    return mid-1
                else:
                    high = mid-1
