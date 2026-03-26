class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        r = k
        while r < len(arr):
            a = abs( arr[r-k] - x ) # first element of window
            b = abs( arr[r] - x ) # upcoming element of window
            if b < a:
                r+=1
            elif b == a:
                if arr[r-k] < arr[r]:
                    return arr[r-k:r]
                else:
                    r+=1
            elif b > a:
                return arr[r-k:r] 
        return arr[-k:]
