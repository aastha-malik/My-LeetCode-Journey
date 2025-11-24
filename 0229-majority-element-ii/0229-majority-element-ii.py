class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums) #O(l)
        l = len(nums)
        s = set()
        n = l / 3
        for k, i in d.items():
            if i > n:
                s.add(k)
        return list(s)
        
        