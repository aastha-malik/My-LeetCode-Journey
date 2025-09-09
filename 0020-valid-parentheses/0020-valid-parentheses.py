class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                res.append(s[i])
            else:
                if len(res) == 0:
                    return False
                if s[i] == ")":
                    if res[-1] == "(":
                        res.pop()
                    else:
                        return False
                elif s[i] == "}":
                    if res[-1] == "{":
                        res.pop()
                    else:
                        return False
                elif s[i] == "]":
                    if res[-1] == "[":
                        res.pop()
                    else:
                        return False
        return len(res) == 0
        
        