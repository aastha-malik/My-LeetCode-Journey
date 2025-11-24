class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        res = set()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i, j in d.items():
            if j > len(nums)/3:
                res.add(i)
        return list(res)
        