class Solution:
    def isValid(self, s: str) -> bool:
        l = s.count("a")
        for i in range(l):
            if "abc" in s:
                s = s.replace("abc", "")
        return s == ""

        