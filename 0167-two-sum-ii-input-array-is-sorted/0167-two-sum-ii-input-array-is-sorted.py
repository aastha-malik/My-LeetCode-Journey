class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        # l = len(numbers)
        # for i in range(l-1):
        #     n = target - numbers[i]
        #     if n in numbers:
        #         for j in range(i+1, l):
        #             if n == numbers[j]:
        #                 return [i+1, j+1]

        