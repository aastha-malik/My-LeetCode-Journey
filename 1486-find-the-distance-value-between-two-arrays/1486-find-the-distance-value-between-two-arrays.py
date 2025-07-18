class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        num = 0
        for i in arr1:
            high = 0
            for j in arr2:
                if abs(i - j) > d:
                    high += 1
            if high == len(arr2):
                num += 1
        return num
        