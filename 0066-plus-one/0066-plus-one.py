class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        s = "".join(digits)
        num = int(s) + 1
        arr  = list(str(num))
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr