class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = nums1 + nums2
        arr.sort()
        res = []
        if arr[0][0] == arr[1][0]:
                res.append([arr[0][0], arr[0][1] + arr[1][1]])
        else:
            res.append([ arr[0][0], arr[0][1] ])

        for i in range(1, len(arr) - 1):
            if arr[i][0] == arr[i + 1][0]:
                res.append([arr[i][0], arr[i][1] + arr[i + 1][1]])
            if arr[i][0] != arr[i + 1][0] and arr[i][0] != arr[i - 1][0]:
                res.append(arr[i])
         
        if arr[-2][0] != arr[-1][0]:
                res.append(arr[-1])

        return res
        

        
        

