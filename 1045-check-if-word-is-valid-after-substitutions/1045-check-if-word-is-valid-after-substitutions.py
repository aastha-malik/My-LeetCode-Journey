class Solution:
    def isValid(self, s: str) -> bool:
        l = s.count("a")
        i = 0
        while i < len(s):
            if s[i:i+3] == "abc":
                s = s[:i] + s[i+3:]

            elif s[i-1:i+2] == "abc":
                s = s[:i-1] + s[i+2:]

            elif s[i-2:i+1] == "abc":
                s = s[:i-2] + s[i+1:]

            elif s[i-3:i] == "abc":
                s = s[:i-3] + s[i:]
            
            else:
                i+= 1

            if s == "abc":
                return True
            
        return s ==""

        