import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        else:
            s = sum(piles)
            low = math.ceil(s / h)
            high = max(piles)
            while low <= high :
                mid = (low + high) // 2
                count = 0
                for i in piles:
                    x = math.ceil(i / mid)
                    count += x
                if count <= h:
                    high = mid-1
                else:
                    low = mid + 1
            return low
                

                    




            