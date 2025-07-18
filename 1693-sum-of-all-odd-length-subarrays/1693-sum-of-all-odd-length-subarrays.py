class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        total = 0
        for i in range(l):
            for j in range(i+1, l+1):
                num = arr[i:j]
                if len(num) % 2 != 0:
                    total += sum(num)
        return total

        