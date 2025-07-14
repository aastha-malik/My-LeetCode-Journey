class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        l = len(operations)
        for i in range(l):
            if operations[i] == "+":
                add = sum([arr[-1], arr[-2]])
                arr.append(add)
            elif operations[i] == "C":
                arr.pop()
            elif operations[i] == "D":
                add = 2 * int(arr[-1])
                arr.append(add)
            else:
                add = int(operations[i])
                arr.append(add)
        
        if len(arr) == 0:
            return 0
        else:
            return sum(arr)
            
        