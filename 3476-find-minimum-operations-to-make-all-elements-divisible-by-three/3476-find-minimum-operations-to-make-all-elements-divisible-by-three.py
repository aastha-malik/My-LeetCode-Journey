class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        arr = []
        for i in nums:
            if i % 3 != 0:
                arr.append(i)
        l = len(arr)
        
        return l                

        