class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        arr = []
        for i in divisors:
            n = 0
            for j in nums:
                if j % i == 0:
                    n += 1
            arr.append(n)
            
        m = max(arr)
        ind = arr.index(m)
        res = divisors[ind]
        for i in range(len(divisors)):
            if m == arr[i]:
                if divisors[i] < res:
                    res = divisors[i]

        return res