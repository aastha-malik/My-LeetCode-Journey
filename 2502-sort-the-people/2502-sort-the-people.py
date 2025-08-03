class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        for i  in range(len(names)):
            arr.append([ heights[i], names[i] ])
        arr.sort(reverse = True)
        res = []
        for i in arr:
            res.append(i[1])
        return res
        