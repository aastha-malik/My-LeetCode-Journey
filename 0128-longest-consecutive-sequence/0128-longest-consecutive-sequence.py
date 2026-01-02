class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        if nums == []:
            return 0
        
        s = set(nums)
        for i in s:
            res = 1
            if i - 1 not in s:
                n = i+1
                while n in s:
                    res += 1
                    n += 1
                ans = max(ans, res)
        return ans
