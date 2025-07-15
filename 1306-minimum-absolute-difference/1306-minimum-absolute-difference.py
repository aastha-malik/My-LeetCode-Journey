class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = arr[1] - arr[0]
        l = len(arr)
        res = []
        for i in range(l-1):
            d = arr[i+1] - arr[i]
            if d < diff:
                diff = d
        for i in range(l-1):
            d = arr[i+1] - arr[i]
            if d == diff:
                res.append([arr[i], arr[i+1]])

                

        return res