class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l-1):
            n = target - numbers[i]
            if n in numbers:
                for j in range(i+1, l):
                    if n == numbers[j]:
                        return [i+1, j+1]

        