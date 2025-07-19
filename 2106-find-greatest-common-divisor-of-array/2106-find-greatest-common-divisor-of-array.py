class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        for i in range(a, 1, -1):
            if a % i == b % i == 0:
                return i
        return 1

        