class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(arr) != len(pattern) :
            return False
        d = {}
        l = 0
        if len(set(arr)) != len(set(pattern)):
            return False
        for i in range(len(arr)):
            d[pattern[i]] = arr[i]
        for i in range(len(arr)):
            if d[pattern[i]] == arr[i]:
                l += 1
        return l == len(pattern)
        