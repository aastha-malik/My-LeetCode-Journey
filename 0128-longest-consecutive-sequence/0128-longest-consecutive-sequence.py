class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        max_len = 1

        for i in s:
            c = 1
            if i-1 not in s:
                
                n = i+1
                while n in s:
                    c += 1
                    n += 1
            max_len = max(max_len,c)
        return max_len
            



