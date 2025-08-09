class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            s = list(str(nums[i]))
            t = 0
            for j in s:
                t += int(j)
            if t == i:
                return i
        return -1

        