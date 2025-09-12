class Solution:
    def isValid(self, s: str) -> bool:
        l = s.count("a")
        if s[0] != "a" or s[-1] != "c":
            return False
        else:
            stack = []
            for i in s:
                stack.append(i)
                if len(stack) >= 3 and stack[-3] + stack[-2]+ stack[-1] == "abc":
                    stack.pop()
                    stack.pop()
                    stack.pop()
            return len(stack) == 0


